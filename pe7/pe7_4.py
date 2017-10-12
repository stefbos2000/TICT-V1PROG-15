def ticker():
    infile = open('pe7_4.txt', 'r')
    regels = infile.readlines()
    infile.close()
    tickerdict = {}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel = tickerregel[0]
        waarde = tickerregel[1].strip()
        tickerdict[sleutel] = waarde
    return tickerdict
print(ticker())
bedrijfsnaam = input('Wat is de bedrijfsnaam? ')
tickbestand = ticker()
for naam in tickbestand:
    if bedrijfsnaam == naam:
        print('Ticker symbol: {}'.format(tickbestand[naam]))
afkorting = input('Wat is de afkorting van het bedrijf? ')
for naam in tickbestand:
    if tickbestand[naam] == afkorting:
        print('Ticker symbol: {}'.format(naam))