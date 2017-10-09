import csv
with open('9.4.csv', 'w') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))
    while True:
        Artikelnummer = input('Wat is het artikelnummer? ')
        if Artikelnummer == '':
            break
        Artikelcode = input('Wat is de artikelcode? ')
        Naam = input('Wat is uw naam? ')
        Voorraad = input('Wat is de voorraad? ')
        Prijs = input('Wat is de prijs? ')
        writer.writerow((Artikelnummer, Artikelcode, Naam, Voorraad, Prijs))