import datetime
import csv

bestand = 'inloggers.csv'

with open('mensen.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    while True:
        achternaam = input("Wat is je achternaam? ")
        if achternaam == 'einde':
            break
        voorletters = input("Wat zijn je voorletters? ")
        geboortedatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((voorletters, achternaam, geboortedatum, email))