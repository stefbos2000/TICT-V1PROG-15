def standaardtarief(afstandKM):
    if afstandKM <= 50:
        standaardtarief = 0.8 * afstandKM
    if afstandKM > 50:
        standaardtarief = afstandKM * 0.6 + 15
    if afstandKM <= 0:
        standaardtarief = 0
    return standaardtarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd > 65 or leeftijd < 12 and weekendrit == 'nee' or weekendrit == 'Nee':
        ritprijs = standaardtarief(afstandKM) * 0.7
    if leeftijd > 65 or leeftijd < 12 and weekendrit == 'ja' or weekendrit == 'Ja':
        ritprijs = standaardtarief(afstandKM) * 0.65
    if leeftijd < 65 and leeftijd > 12 and weekendrit == 'nee' or weekendrit == 'Nee':
        ritprijs = standaardtarief(afstandKM)
    if leeftijd < 65 and leeftijd > 12 and weekendrit == 'ja' or weekendrit == 'Ja':
        ritprijs = standaardtarief(afstandKM) * 0.6
    return ritprijs

afstandKM = eval(input('Wat is de afstand in kilometers? '))
leeftijd = eval(input('Wat is uw leeftijd? '))
weekendrit = input('Reist u in het weekend? ')

s = ('De totale prijs die u moet betalen is ' + str(ritprijs(leeftijd, weekendrit, afstandKM)) + ' euro')
print(s)