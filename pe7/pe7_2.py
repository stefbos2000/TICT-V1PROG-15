while True:
    woord = input('Welk woord kiest u? ')
    if len(woord) == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(woord))
        break
    else