#   S A P - R E N T E     #
#   -------------------   #
#   bernie   16.05.2021   #
#   -------------------   #

"""
Zweck: Dieses Projekt dient der Ermittlung des letzten Arbeitstages bei SAP
Python-Version: 3.9
Schnittstellen: Shell, Tk/Tcl (GUI), evtl. ReST (geplant)
"""

# Datumsfunktionen einbinden
import datetime
from datetime import date

# GUI-Toolkit TK einbinden
import tkinter as tk
from tkinter import *


def datumsumwandlung_date(jahr, monat, tag):
    """ wandelt das eingeg. Datum in date-Format um """
    rar2 = datetime.date(year=jahr,
                         month=monat,
                         day=tag)
    return rar2


def typencheck(eingabe, typ, text):
    """ überprüft eingeg. Wert auf korrektes Type-Format """
    """ Text-only Ein-/Ausgabe """
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
    else:
        print("*** ERROR in typencheck ***")
    return ausgabe


def datum_tage_brutto(datum_alt, tage):
    """ ermittelt aus Tagen eine neues Datum """
    # da wir nicht den ersten Rententag, sondern den letzten Arbeitstag ausrechnen, addieren wir 1 freien Tag
    tage = tage + 1
    datum_neu = datum_alt - datetime.timedelta(tage)
    return datum_neu


def datum_tage_netto(datum_alt, tage, firedays):
    """ ermittelt aus Tagen eine neues Datum """
    # um die Wochenenden zu berücksichtigen, werden die Tage mit 1.4 multipliziert,
    # denn: 5 x 1,4 = 7
    faktor = 1.4
    # da wir nicht den ersten Rententag, sondern den letzten Arbeitstag ausrechnen, addieren wir 1 freien Tag
    tage_hochgerechnet = (tage * faktor) + firedays + 1
    datum_neu = datum_alt - datetime.timedelta(tage_hochgerechnet)
    return datum_neu


def umwandler_int(eingabe):
    """ Umwandlung einer Eingabe in den Typ Integer """
    ausgabe = int(eingabe.get())
    print("Tag: ", ausgabe)
    return ausgabe


# Beginn Hauptprogramm
heute = date.today()
rar_tag = 0
# rar_tag2 = 0
rar_monat = 0
rar_jahr = 0
resturlaub_t = 0
azk_h = 0
feiertage = 0
# Ein-/Ausgabe nur via Text-Konsole:
print("Willkommen zum Projekt SAP-RENTE!\t\t\t\t\t",heute)
print("\nPARAMETER-EINGABE")
print("Beginn der Regelaltersrente gem. Rentenauskunft:")

rar_tag = typencheck(rar_tag, "int", "Tag: \t ")
rar_monat = typencheck(rar_monat, "int", "Monat: \t ")
rar_jahr = typencheck(rar_jahr, "int", "Jahr: \t ")
rar = datumsumwandlung_date(rar_jahr, rar_monat, rar_tag)
resturlaub_t = typencheck(resturlaub_t, "float", "\nResturlaub in Tagen (Punkt als Separator): \t\t\t\t\t\t ")
azk_h = typencheck(azk_h, "float", "gesammelte h im AZK gem. Gehaltszettel (Punkt als Separator): \t ")
feiertage = typencheck(feiertage, "int", "evtl. Anzahl zu berücksichtigender Feiertage: \t\t\t\t\t ")
tage1 = rar - heute
tage2 = resturlaub_t + (azk_h // 8)
brutto_datum = datum_tage_brutto(rar, tage2)
print("\nERGEBNIS")
netto_datum = datum_tage_netto(rar, tage2, feiertage)
print("letzter Arbeitstag mit Berücksichtigung von Wochenenden und eingegebenen Feiertagen (JJJJ-MM-TT): ", netto_datum)
