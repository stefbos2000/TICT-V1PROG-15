import datetime
vandaag = datetime.datetime.today()
datum = vandaag.strftime('%a %d %b 20%y,')
tijd = vandaag.strftime('%H: %M: %S,')
naam = input('Hoe heet de hardloper? ')
outfile = open('hardlopers.txt', 'a')
outfile.write('{},{},{}'.format(datum, tijd, naam))
outfile.close()