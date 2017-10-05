infile = open('pe5_2.txt', 'r')
inhoud = infile.readlines()
a = len(inhoud)
for regel in inhoud:
    info = regel.split(', ')
    s = info[0], info[1] = info[1], info[0]
kaartnummer = max()
regel = inhoud.index(kaartnummer) + 1

print('Deze file telt ' + str(a) + ' regels')
print('Het grootste kaartnummer is: ' + str(kaartnummer.strip()) + ' en dat staat op regel ' + str(regel))