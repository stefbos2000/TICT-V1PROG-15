def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluisinfo = infile.readlines()
    regels = 12 - len(kluisinfo)
    infile.close()
    print('Het aantal vrije kluizen zijn: {}'.format(regels))
def nieuwe_kluis():
    kluizen = []
    infile = open('kluizen.txt', 'r')
    kluizenvrij = infile.read()
    infile.close()
    kluizenregels = kluizenvrij.split('\n')
    L = []
    for regel in kluizenregels:
        L.append(regel.split(';'))
    for nummer in L[0]:
        kluizen.append(nummer)
    print(kluizen)
    if kluizen is not []:
        (input('Wat is uw code voor uw kluis? '))
    else:
        print('Er zijn helaas geen kluizen meer beschikbaar. ')
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
        code = gegevensvankluis[1]
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