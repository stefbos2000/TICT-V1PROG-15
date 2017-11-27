def eindbedrag(bedrag, rentepercentage):
    eindbedrag = bedrag + ((rentepercentage * bedrag) / 100)
    print('Het eindbedrag over een jaar is {}'.format(eindbedrag))
bedrag = eval(input('Wat is het bedrag? '))
rentepercentage = eval(input('Wat is het rentepercentage? '))
eindbedrag(bedrag, rentepercentage)