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