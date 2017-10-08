def seizoen(maandnummer):
    if maandnummer == 3 or maandnummer == 4 or maandnummer == 5:
        print('Het is lente')
    elif maandnummer == 6 or maandnummer == 7 or maandnummer == 8:
        print('Het is zomer')
    elif maandnummer == 9 or maandnummer == 10 or maandnummer == 11:
        print('Het is herfst')
    elif maandnummer == 12 or maandnummer == 1 or maandnummer == 2:
        print('Het is winter')
    else:
        print('Geen geldig maandnummer')
maandnummer = eval(input('Welk maandnummer is het? '))
seizoen(maandnummer)