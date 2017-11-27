infile = open('pe5_22.txt', 'r')
regels = infile.readlines()
infile.close()
outfile = open('pe5_22.txt', 'w')
for regel in regels:
    kaartinfo = regel.split(', ')
    outfile.write(' {} heeft kaartnummer: {}\n'.format(kaartinfo[1].strip(), kaartinfo[0]))