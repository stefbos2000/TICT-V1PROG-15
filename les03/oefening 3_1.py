naam = input('What is you name: ')
leeftijd = eval(input('What is your age: '))
if leeftijd >= 18:
    print(naam + ', je mag stemmen')
else:
    print(naam + ', je mag niet stemmen')