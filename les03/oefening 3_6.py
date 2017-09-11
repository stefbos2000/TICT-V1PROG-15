getallenrij = [6, 4, 8, 1, 65, 2, 32, 5]
vraag = eval(input('Wat voor getal kies je? '))
gevonden = False
for getal in getallenrij:
    if getal == vraag:
        gevonden = True
if gevonden == True:
    print('Het vraaggetal zit in de getallenrij.')
else:
    print('Het vraaggetal zit niet in de getallenrij.')