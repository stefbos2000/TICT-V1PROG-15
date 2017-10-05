cijfers = {'Sander': 4, 'San': 5, 'Henk': 6, 'Martijn': 8, 'Adriaan': 3, 'Pieter': 9, 'Stef': 10, 'Hans': 1}
for cijfer in cijfers:
    if cijfers[cijfer] > 9:
        print('De mensen met een cijfer hoger dan een 10 zijn: {}: {}.'.format(cijfer, cijfers[cijfer]))