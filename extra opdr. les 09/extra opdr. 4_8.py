tabel = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
for rij in tabel:
    for getal in rij:
        if getal%2 == 0:
            print(getal, end= ' ')
    print()