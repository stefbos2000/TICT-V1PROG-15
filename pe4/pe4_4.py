def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) > 6:
        print(True)
    else:
        print(False)
    return new_password
oldpassword = input('Wat is je oude wachtwoord? ')
newpassword = input('Wat is je nieuwe wachtwoord? ')
new_password(oldpassword, newpassword)