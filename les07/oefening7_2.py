week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do':'donderdag', 'vr': 'vrijdag'}
print(week)
print('ma' in week)
print(week['ma'])
week['di'] = 'dinsdag'
print(week)
week['za'] = 'zaterdag'
print(week)

for afkorting in week.keys():
    print(afkorting)

for langeNaam in week.values():
    print(langeNaam)

for beide in week.items():
    print(beide)

for afkorting in week.keys():
    print(afkorting, week[afkorting])

for afkorting in week:
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))