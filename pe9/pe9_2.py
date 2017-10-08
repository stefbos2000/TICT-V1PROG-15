import datetime
import csv
bestand = 'inloggers.csv'
achternaam = input("Wat is je achternaam? ")
voorletters = input("Wat zijn je voorletters? ")
geboortedatum = input("Wat is je geboortedatum? ")
email = input("Wat is je e-mail adres? ")
while achternaam != 'einde':
    bestand = 'inloggers.csv'
    achternaam = input("Wat is je achternaam? ")
    voorletters = input("Wat zijn je voorletters? ")
    geboortedatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
while achternaam == 'einde':
    break