#   S A P - R E N T E     #
#   -------------------   #
#   bernie   23.07.2021   #
#   -------------------   #

"""
Zweck: Dieses Progrmm dient der Ermittlung des letzten Arbeitstages bei SAP
Python-Version: 3.9
Schnittstellen: Shell (Konsole), Tk/Tcl (Gui)
Konsolenversion
"""

# Datumsfunktionen einbinden
import datetime
from datetime import date

def datumsumwandlung_date(jahr, monat, tag):
    """ wandelt das eingeg. Datum in date-Format um """
    datum = datetime.date(year=jahr,
                         month=monat,
                         day=tag)
    print(datum.strftime("-> %A %d. %B %Y"))
    return datum

def typencheck(eingabe, typ, text):
    """ überprüft eingeg. Wert auf korrektes Type-Format """
    if (typ == 'int'):
        dummy_int = 0
        while isinstance(dummy_int, int):
            try:
                dummy_int = int(input(text))
                break
            except:
                pass
        ausgabe = dummy_int
    elif (typ == 'float'):
        dummy_float = 0.0
        while isinstance(dummy_float, float):
            try:
                dummy_float = float(input(text))
                break
            except:
                pass
        ausgabe = dummy_float
    elif (typ == 'date'):
        datumunbekannt = True
        while datumunbekannt == True:
            try:
                rar_tag = int(eingabe[0:2])
                rar_monat = int(eingabe[3:5])
                rar_jahr = int(eingabe[6:10])
                ausgabe = datumsumwandlung_date(rar_jahr, rar_monat, rar_tag)
                datumunbekannt = False
            except ValueError:
                datumunbekannt = True
                eingabe = input("Datum bitte im Format TT.MM.JJJJ eingeben: ")
    else:
        print("*** ERROR in typencheck ***")
    return ausgabe

def datum_tage_netto(datum_alt, tage, firedays):
    """ ermittelt aus Tagen eine neues Datum """
    # um die Wochenenden zu berücksichtigen, werden die Tage mit 1.4 multipliziert,
    # denn: 5 x 1,4 = 7
    faktor = 1.4
    # da wir nicht den ersten Rententag, sondern den letzten Arbeitstag ausrechnen, addieren wir 1 Tag
    tage_hochgerechnet = (tage * faktor) + firedays + 1
    datum_neu = datum_alt - datetime.timedelta(tage_hochgerechnet)
    # Prüfung auf Wochentag: fällt Datum auf Wochenende, wird der vorherige Fr. gezogen
    if (datum_neu.weekday() == 5):
        datum_netto = datum_neu - datetime.timedelta(1)
    elif (datum_neu.weekday() == 6):
        datum_netto = datum_neu - datetime.timedelta(2)
    else:
        datum_netto = datum_neu
    return datum_netto

def ergebnis_ausgabe(datum):
    """ Ausgabe des ermittelten Datums """
    print("\nERGEBNIS")
    print("--------")
    print("letzter Arbeitstag mit Berücksichtigung von WE und eingeg. Feiertagen: ", datum.strftime("%A %d. %B %Y"))
    print("Bem.: ohne Gewähr, gewisse Unschärfen müssen akzeptiert werden!\n")

# Beginn Hauptprogramm
heute = date.today()
resturlaub_t = 0
azk_h = 0
feiertage = 0
# Ein-/Ausgabe nur via Text-Konsole:
print("Willkommen zum Projekt SAP-Rentner! - wann bin ich dran? \t ", heute)
print("\nPARAMETER-EINGABE")
rar_datum_string = input("Beginn der Regelaltersrente gem. Rentenauskunft (TT.MM.JJJJ): \t ")
rar = typencheck(rar_datum_string, "date", "Datum (TT.MM.JJJJ): \t ")
resturlaub_t = typencheck(resturlaub_t, "float", "Resturlaub in Tagen (Punkt als Separator): \t ")
azk_h = typencheck(azk_h, "float", "gesammelte h im AZK (Punkt als Separator): \t ")
feiertage = typencheck(feiertage, "int", "evtl. Anzahl zu berücksichtigender Feiertage: \t ")
# tage1 = rar - heute
tage = resturlaub_t + (azk_h // 8)
netto_datum = datum_tage_netto(rar, tage, feiertage)
ergebnis_ausgabe(netto_datum)

# ENDE