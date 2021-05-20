#   S A P - R E N T E     #
#   -------------------   #
#   bernie   20.05.2021   #
#   -------------------   #

"""
Zweck: Dieses Projekt dient der Ermittlung des letzten Arbeitstages bei SAP
Python-Version: 3.9
Schnittstellen: Shell (Konsole), Tk/Tcl (geplant), evtl. ReST (geplant)
"""

# Datumsfunktionen einbinden
import datetime
from datetime import date

def datumsumwandlung_date(jahr, monat, tag):
    """ wandelt das eingeg. Datum in date-Format um """
    datum = datetime.date(year=jahr,
                         month=monat,
                         day=tag)
    return datum

def typencheck(eingabe, typ, text):
    """ überprüft eingeg. Wert auf korrektes Type-Format """
    """ funktioniert nicht korrekt bei Typ date """
    if typ == 'int':
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
        dummy_date = date.today()
        while isinstance(dummy_date, date):
            try:
               dummy_date = isinstance(input(text), datetime)
               break
            except:
                pass
        ausgabe = dummy_date
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
    return datum_neu

def ergebnis_ausgabe(datum):
    """ Ausgabe des ermittelten Datums """
    print("\nERGEBNIS")
    print("--------")
    print("letzter Arbeitstag mit Berücksichtigung von Wochenenden und eingeg. Feiertagen (JJJJ-MM-TT): ", datum)
    print("Bem.: ohne Gewähr, gewisse Unschärfen müssen akzeptiert werden!\n")

# Beginn Hauptprogramm
heute = date.today()
rar_datum = heute
resturlaub_t = 0
azk_h = 0
feiertage = 0
# Ein-/Ausgabe nur via Text-Konsole:
print("Willkommen zum Projekt SAP-Rentner! - wann bin ich dran?\t\t\t\t\t", heute)
print("\nPARAMETER-EINGABE")
print("Beginn der Regelaltersrente gem. Rentenauskunft:")
# rar_datum = typencheck(rar_datum, "date", "\t Datum (JJJJ-MM-TT): \t ")
# rar_tag = typencheck(rar_tag, "int", "\tTag (1-31): \t ")
# rar_monat = typencheck(rar_monat, "int", "\tMonat (1-12): \t ")
# rar_jahr = typencheck(rar_jahr, "int", "\tJahr: \t\t\t ")
rar_datum_string = input("Datum (JJJJ-MM-TT): ")
rar_jahr = int(rar_datum_string[0:4])
rar_monat = int(rar_datum_string[5:7])
rar_tag = int(rar_datum_string[8:10])
rar = datumsumwandlung_date(rar_jahr, rar_monat, rar_tag)
resturlaub_t = typencheck(resturlaub_t, "float", "Resturlaub in Tagen (Punkt als Separator): \t\t ")
azk_h = typencheck(azk_h, "float", "gesammelte h im AZK (Punkt als Separator): \t\t ")
feiertage = typencheck(feiertage, "int", "evtl. Anzahl zu berücksichtigender Feiertage: \t ")
tage1 = rar - heute
tage2 = resturlaub_t + (azk_h // 8)
netto_datum = datum_tage_netto(rar, tage2, feiertage)
ergebnis_ausgabe(netto_datum)
# ENDE