def eindbedrag(bedrag, rentepercentage):
    eindbedrag = bedrag + ((rentepercentage*bedrag)/100)
    return eindbedrag
bedrag = eval(input('Wat is het bedrag? '))
rentepercentage = eval(input('Wat is het rentepercentage? '))
antwoord = eindbedrag(bedrag, rentepercentage)
print('Het eindbedrag over een jaar is {}'.format(antwoord))