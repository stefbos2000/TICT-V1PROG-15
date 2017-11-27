def berekensomevengetallen():
    getallenrij1 = [1, 5, 6, 3, 5, 3, 234, 4, 2]
    somevengetallen = 0
    for getal in getallenrij1:
        if getal%2 == 0:
            somevengetallen = somevengetallen + getal
    return somevengetallen
def berekensomonevengetallen():
    getallenrij2 = [1, 5, 6, 3, 5, 3, 234, 4, 2]
    somonevengetallen = 0
    for getal in getallenrij2:
        if getal % 2 == 1:
            somonevengetallen = somonevengetallen + getal
    return somonevengetallen
print('De som van de evengetallen bedraagt {}'.format(berekensomevengetallen()))
print('De som van de onevengetallen bedraagt {}'.format(berekensomonevengetallen()))