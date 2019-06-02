class Log(object): 
    __instance = None

    def __init__(self):
        pass

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance 

    
    def __str__(self):
        pass

    def __del__(self):
        pass

log1 = Log()
log2 = Log()
print(log1 == log2)  
print("log1 address: %s, log2 address %s" %(id(log1), id(log2)) )

    
