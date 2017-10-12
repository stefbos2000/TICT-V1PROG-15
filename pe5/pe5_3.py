infile = open('pe5_2.txt', 'r')
inhoud = infile.readlines()
infile.close()
a = len(inhoud)
regelnummer = 0
grootstenummer = 0
for regel in inhoud:
    info = regel.split(',')
    nummer = int(info[0])
    regelnummer += 1
    if nummer > grootstenummer:
        grootstenummer = nummer
        grootsteregelnummer = regelnummer
print('Deze file telt {} regels'.format(a))
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(grootstenummer, grootsteregelnummer))