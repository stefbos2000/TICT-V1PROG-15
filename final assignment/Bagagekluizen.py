def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluisinfo = infile.readlines()
    regels = 12 - len(kluisinfo)
    infile.close()
    print('Het aantal vrije kluizen zijn: {}'.format(regels))

def nieuwe_kluis():
    # maak een lijst met de getallen 1 tot en met 12 die de kluisnummers voorstellen
    kluisnummers = []
    for i in range(1, 13):
        kluisnummers.append(i)

    # het inlezen van kluizen.txt in een list kluizendata met readlines()
    # elk element van de lijst is een regel uit kluizen.txt
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()

    # alle regels van kluizendata worden doorlopen
    for kluis in kluizendata:
        # doorlopen van kluizendata en elke regel van kluizendata splitsen op ';'
        gegevensvan1kluis = kluis.split(';')
        # elke regel bestaat uit twee elementen waarvan het 1e element het nummer is;
        # let op: dit element komt uit een bestand en is dus een string, vandaar stringnummer
        stringnummer = gegevensvan1kluis[0]
        # stringnummer converteren naar een int en toekennen aan nummer
        nummer = int(stringnummer)
        # het element met de waarde nummer uit kluizendata verwijderen
        kluisnummers.remove(nummer)

    # nu bevat kluizendata alleen nummers die nog niet in gebruik zijn
    if len(kluisnummers) > 0:
        # pak het eerste element van kluizendata en dit is het nummer van de kluis
        nieuwkluisnummer = kluisnummers[0];
        # laat dit nummer aan de gebruiker weten
        print('Je kluisnummer is {}'.format(nieuwkluisnummer))
        # vraag de gebruiker om een code in te voeren
        code = input('Voer een code in: ')
        # open het bestand kluizen.txt om een nieuwe kluis toe te voegen met append
        outfile = open('kluizen.txt', 'a')
        # schrijf het nummer en de code in het tekstbestand gescheiden door een ';'
        # omdat append is gebruikt, worden nummer en code achteraan het bestand toegevoegd
        outfile.write('{};{}\n'.format(nieuwkluisnummer, code))
        # sluit het tekstbestand
        outfile.close()
    else:
        # alle kluizen zijn bezet
        print('Er is geen kluis meer beschikbaar')

def kluis_openen():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringkluisnummer = input('Wat is je nummer? ')
    kluiscode = input('Wat is je code? ')
    gegevenscorrect = False
    for regel in kluizendata:
        gegevensvankluis = regel.split(';')
        stringkluisnummer = gegevensvankluis[0]
        code = gegevensvankluis[1].strip()
        if stringkluisnummer == stringkluisnummer and kluiscode == code:
            gegevenscorrect = True
    if gegevenscorrect:
        print('correct')
    else:
        print('niet correct')

print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('(4: Ik geef mijn kluis terug)')
keuze = eval(input('Geef het nummer van uw keuze: '))
if keuze is 1:
    toon_aantal_kluizen_vrij()
elif keuze is 2:
    nieuwe_kluis()
elif keuze is 3:
    kluis_openen()