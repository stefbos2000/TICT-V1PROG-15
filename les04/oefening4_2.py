def rng (lijst):
    verschil = max(lijst) - min(lijst)
    return verschil
lijst = [4, 0, 1, -2]
res = rng (lijst)
print(res)