import random
def monopolyworp():
    dobbelsteen1 = random.randrange(1, 7)
    dobbelsteen2 = random.randrange(1, 7)
    som = dobbelsteen1 + dobbelsteen2
    print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, som))
    while dobbelsteen1 == dobbelsteen2:
        print(som)
        break
monopolyworp()