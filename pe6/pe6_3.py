invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lossegetallen = invoer.split('-')
getallenlijst = []
for stringgetal in lossegetallen:
    getal=int(stringgetal)
    getallenlijst.append(getal)
maxi = max(lossegetallen)
mini = min(lossegetallen)
aantal = len(getallenlijst)
somgetal = sum(getallenlijst)
gemiddelde = sum(getallenlijst)/len(getallenlijst)

print('Gesorteerde list van ints:  {}'.format(getallenlijst))
print('Grootste getal: {} en Kleinste getal: {}'.format(maxi, mini))
print('Aantal getallen: {} en Som van de getallen: {}'.format(aantal, somgetal))
print('Gemiddelde: {}'.format(gemiddelde))