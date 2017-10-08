som = 0
aantal = 0
getal = eval(input('Welk cijfer kiest u? '))
while getal != 0:
    som = som + getal
    getal = eval(input('Welk cijfer kiest u? '))
    aantal = getal+1
print('Er zijn {} getallen ingevoerd, de som is: {}'.format(aantal, som))