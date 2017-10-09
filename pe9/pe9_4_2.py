import csv
with open('9.4_2.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    duursteartikel = 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > duursteartikel:
            duursteartikel = prijs
            duurstenaam = row['Naam']
    print('Het duurste artikel is Monitorstandaard en die kost {} Euro'.format(duursteartikel))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(duursteartikel, duursteartikel))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(duursteartikel))