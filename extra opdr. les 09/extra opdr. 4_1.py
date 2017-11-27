temp = eval(input('Welke temp is het vandaag? '))
if temp <= 0:
    print('Het vriest vandaag.')
elif temp >= 0 and temp <= 15:
    print('Het is koud vandaag.')
elif temp >= 15:
    print('Het is lekker weer vandaag.')