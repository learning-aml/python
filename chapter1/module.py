#import
#from ** import
#from ** import *
#as
#

def isnull(str):
    if not str:
        return True
    elif str.strip() == "":
        return True
    else:
        return False


from . import isnull
print(isnull("as"))