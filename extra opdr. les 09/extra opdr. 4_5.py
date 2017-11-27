getallenrij = [1, 5, 6, 3, 5, 3, 234, 4, 2]
somevengetallen = 0
for getal in getallenrij:
    if getal%2 == 0:
        somevengetallen = somevengetallen + getal
print(somevengetallen)