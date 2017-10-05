import datetime
import csv
def kek():
    bestand = 'inloggers.csv'
    achternaam = input("Wat is je achternaam? ")
    voorletters = input("Wat zijn je voorletters? ")
    geboortedatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
#gebruik hier een herhalingslus:
    while achternaam != 'einde':
        kek()
    while achternaam == 'einde':
        break
    return achternaam
kek()
#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file
csv.writer()