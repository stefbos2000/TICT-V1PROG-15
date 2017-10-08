def inlezen_beginstation(stations):
    beginstation = input('Wat is je beginstation? ')
    while beginstation not in stations:
        print('Dit beginstation is niet geldig')
        beginstation = input('Wat is je beginstation? ')
    return beginstation

def inlezen_eindstation(stations, beginsstation):
    eindstation = input('Wat is je eindstation? ')
    while eindstation not in stations:
        print('Dit eindstation is niet geldig')
        eindstation = input('Wat is je eindstation? ')
    while (stations.index(beginstation)) > (stations.index(eindstation)):
        print('Dit eindstation is niet geldig')
        eindstation = input('Wat is je eindstation? ')
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, lbeginstation))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, leindstation))
    print('De afstand bedraagt {} station(s).'.format(afstand))
    print('De prijs van het kaartje is {} euro'.format(prijs))
    print('')
    print('Jij stapt in de trein in: {}'.format(beginstation))
    print('')
    print('Jij stapt uit in: {}'.format(eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraaal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hetrogenbosch', 'Eindhoven', 'Weert', 'Roermand', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
lbeginstation = stations.index(beginstation) + 1
leindstation = stations.index(eindstation) + 1
afstand = leindstation-lbeginstation
prijs = 5*(afstand)
omroepen_reis(stations, beginstation, eindstation)