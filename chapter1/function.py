def sign(x):
    if x>0:
        return 'positive'
    elif x<0:
        return 'negative'
    else:
        return 'zero'

for x in [-1,0,1]:
    print (sign(x))

def hello(name, loud=False):
    if loud:
        print ('HELLO, %s!' % name.upper())
    else:
        print ('Hello, %s' % name)
hello('BoB')
hello('fred', True)


def f1(x):
    def f2(y):
        return y ** x
    return f2
