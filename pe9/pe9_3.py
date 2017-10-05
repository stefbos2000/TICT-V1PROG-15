import csv
with open('gamers2.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    max = 0
    dat = ''
    na = ''
    for row in reader:
        maxi = max + int(row[2])
        datum = dat + str(row[1])
        naam = na + str(row[0])
    print('De hoogste score is: {} op {} behaald door {}'.format(maxi, datum, naam))