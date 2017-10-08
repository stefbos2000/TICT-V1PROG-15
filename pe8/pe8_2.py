import random
def monopolyworp():
    dobbelsteen1 = random.randrange(1, 7)
    dobbelsteen2 = random.randrange(1, 7)
    som = dobbelsteen1 + dobbelsteen2
    while dobbelsteen1 == dobbelsteen2:
        print('{} + {} = {} (dubbel)'.format(dobbelsteen1, dobbelsteen2, som))
        dobbelsteen1 = random.randrange(1, 7)
        dobbelsteen2 = random.randrange(1, 7)
        som = dobbelsteen1 + dobbelsteen2
    while dobbelsteen1 != dobbelsteen2:
        print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, som))
        break
        while dobbelsteen1 == dobbelsteen2:
            print('{} + {} = {} (dubbel)'.format(dobbelsteen1, dobbelsteen2, som))
            dobbelsteen1 = random.randrange(1, 7)
            dobbelsteen2 = random.randrange(1, 7)
            som = dobbelsteen1 + dobbelsteen2
        while dobbelsteen1 != dobbelsteen2:
            print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, som))
            break
            while dobbelsteen1 == dobbelsteen2:
                print('{} + {} = {} (ga naar de gevangenis)'.format(dobbelsteen1, dobbelsteen2, som))
                dobbelsteen1 = random.randrange(1, 7)
                dobbelsteen2 = random.randrange(1, 7)
                som = dobbelsteen1 + dobbelsteen2
            while dobbelsteen1 != dobbelsteen2:
                print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, som))
                break
monopolyworp()