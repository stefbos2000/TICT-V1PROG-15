getallenrij = [6, 4, 8 ,1, 3, 2, 32, 5]
aantal3 = 0
for getal in getallenrij:
    if getal%3 == 0:
        aantal3 = aantal3 + 1
print('Het aantal getallen deelbaar door 3 is: ' + str(aantal3))