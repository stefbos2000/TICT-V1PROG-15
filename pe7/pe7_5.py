def namen():
    namendict = {}
    naam = input('Volgende naam: ')
    while naam != '':
        if naam in namendict:
            namendict[naam] += 1
        else:
            namendict[naam] = 1
        naam = input('Volgende naam: ')
    print(namendict)
namen()