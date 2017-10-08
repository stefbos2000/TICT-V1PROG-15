lijststring = eval(input('geef een lijst met minimaal 10 strings: '))
for woord in lijststring:
    if len(woord) == 4:
        lijst = [woord]
        print('De nieuw-gemaakte lijst met alle vier-letter strings is: {}'.format(lijst))


['hond', 'kat', 'paard', 'mand', 'raam', 'bezem', 'laptop', 'hand', 'been', 'voet', 'hoofd']