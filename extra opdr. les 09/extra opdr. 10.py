def maaknieuwetabel(tabel):
    evengetal = 0
    for rij in tabel:
        for getal in rij:
            if getal%2 == 0:
                evengetal = getal + 1
    onevengetal = 0
    for rij in tabel:
        for getal in rij:
            if getal%2 == 1:
                onevengetal = getal -1
    print(evengetal)
    print(onevengetal)
tabel = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
maaknieuwetabel(tabel)