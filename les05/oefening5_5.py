infile = open('voorbeeld5_5.txt', 'r')
inhoud = infile.read()
infile.close()
print(inhoud)

infile = open('voorbeeld5_5.txt', 'r')
inhoud = infile.read()
infile.close()
a = inhoud.split()
print(a)

infile = open('voorbeeld5_5.txt', 'r')
inhoud = infile.readlines()
infile.close()
print(inhoud)