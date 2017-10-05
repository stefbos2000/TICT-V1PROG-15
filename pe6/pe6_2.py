lijststring = eval(input('geef een lijst met minimaal 10 strings: '))
['hond', 'kat', 'paard', 'mand', 'raam', 'bezem', 'laptop', 'hand', 'been', 'voet', 'hoofd']
for woord in lijststring:
    if len(woord) is 4 in lijststring:
        print('De nieuw-gemaakte lijst met alle vier-letter strings is: [{}]').format(woord)