infile = open('pe5_2.txt', 'r')
inhoud = infile.readlines()
infile.close()
for regel in inhoud:
    info = regel.split(', ')
    print(' {} heeft kaartnummer: {} '.format(info[1].strip(), info[0]))