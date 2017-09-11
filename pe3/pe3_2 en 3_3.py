leeftijd = eval(input('Geef je leeftijd: '))
paspoort = (input('Heb je een nederlands paspoort? '))
if (leeftijd > 18) and (paspoort == 'ja' or 'Ja'):
    print('Gefeliciteerd!, je mag stemmem!')
else:
    print('Helaas, je mag niet stemmen')