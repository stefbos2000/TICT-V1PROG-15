try:
    def inValues():
        nummer = eval(input('geef een nummer: '))
    inValues()
except NameError:
    nummer = eval(input('Geef een nummer: '))
    print('Er is geen getal ingevoerd')