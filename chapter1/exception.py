try:
    a = 1
    print(a)
    i = 1/0
    print("hello")
except (NameError, ZeroDivisionError) as ex:
    print("error")
    print(ex)

class PasswordException(Exception):
    def __init__(self, pw, min_len):
        self.password=pw
        self.min_len=min_len

    def __str__(self):
        return "%s password error, min length %s" %(self.password, self.min_len)
    

def reg(username, pasword):
    if len(pasword) < 6:
        raise PasswordException(pasword, 6)
    else:
        print("user name: %s, password: %s" %(username, pasword))        


try:
    reg("zs", "1233333")
except PasswordException as ex :
    print(ex)        
finally:
    print("finally")
#except Exception as ex:
#    print(ex)
