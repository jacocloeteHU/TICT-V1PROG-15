def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    else :
        return False

print(str(new_password('jaco','asd33333')))

print(str(new_password('jaco','asa')))
print(str(new_password('asd33333','asd33333')))


def new_passwordnew(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:

        for c in newpassword:
            if c in '0123456789':
                return True
        return False
    else :
        return False

print(str(new_passwordnew('jaco','asd33333')))

print(str(new_passwordnew('jaco','asa')))
print(str(new_passwordnew('asd33333','asd33333')))
