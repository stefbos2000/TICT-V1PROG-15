gewicht = eval(input('Wat is uw gewicht? '))
lengte = eval(input('Wat is uw lengte? '))
BMI = gewicht/lengte**2
print('uw BMI is ' + str(BMI) + '.')
if BMI <= 18.5:
    print('ondergewicht')
if BMI > 18.5 or BMI <= 25:
    print('normaal')
else:
    print('overgewicht')