import random
def diceprob(getal):
    aantalworpinv = 0
    aantalworp = 0
    while aantalworpinv < 100:
        aantalogen1 = random.randrange(1, 7)
        aantalogen2 = random.randrange(1, 7)
        som = aantalogen1 + aantalogen2
        if som == getal:
            aantalworpinv += 1
        aantalworp += 1
    print(aantalworp)
getal = eval(input('welk getal van 1 tot er met 12 kiest u? '))
diceprob(getal)