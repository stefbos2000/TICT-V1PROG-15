def kwadraten_som(grondgetallen):
    kwadraten = 0
    for getal in grondgetallen:
        if getal >=0:
            kwadraten = kwadraten + getal**2
    return kwadraten
grondgetallen = [4, 5, 6, 7, 2, 10]
nummers = kwadraten_som(grondgetallen)
print(nummers)