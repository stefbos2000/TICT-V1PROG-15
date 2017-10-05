def convert(tempC):
    tempF = tempC * 1.8 + 32
    return tempF

def table():
    for tempC in range(-30, 41, 10):
        print('{:5} {:3}'.format(convert(tempC), tempC))
    return tempC
table()