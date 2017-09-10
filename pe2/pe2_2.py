cijferICOR = 6
cijferPROG = 6
cijferCSN = 7
gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3
print(gemiddelde)
beloning = 30 * (cijferPROG + cijferICOR + cijferCSN)
print(beloning)
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van $' + str(beloning) + '.0 op!'
print(overzicht)