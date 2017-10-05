try:
    personen = eval(input('Hoeveel personen gaan er mee? '))
    prijs = 4356
    totaleprijs = prijs/personen
    if personen < 0:
        print('Negatieve getallen zijn niet toegestaan')
    else:
        print('De prijs per persoon wordt: {}'.format(totaleprijs))
except ZeroDivisionError:
    print('U kunt niet met 0 personen op vakantie gaan.')
except NameError:
    print('Strings zijn niet toegestaan als cijfers')
except SyntaxError:
    print('Ongeldige invoer')