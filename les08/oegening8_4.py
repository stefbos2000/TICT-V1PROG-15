string = input('Welke string kiest u? ')
for letter in string:
    code = ord(letter)
    print('{} {:4} {:x} {:b}'.format(letter, code, code, code))