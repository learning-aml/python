#class    Greeter(object):
#    def __init__(self, name):
#     self.name= name 
#    
#    def greet(self, loud=False):
#        if loud:
#            print ('HELLO, %s!' % self.name.upper())
#        else:
#            print ('Hello, %s' % self.name)
#
#g = Greeter('Fred')  # Construct an instance of the Greeter class
#g.greet()            # Call an instance method; prints "Hello, Fred"
#g.greet(loud=True)


class A():
    def test(self):
        print("a test")

class B():
    def test(self):
        print("b : test")

class C(A, B):
    def __init__(self):
        super().__init__()

    def test1(self):
        print("c: test")

c = C()
print(C.__mro__)
c.test()


class User(object):
    name="zzh"  #公有类属性
    __passwd="123456" #私有类属性

    def __init__(self, sex, username):
        print("init called")
        self.sex=sex
        self.username=username

    def __new__(cls, username, password):
        print("new called")
        return object.__new__(cls)

    def __str__(self):
        return "username: %s, password: %s" %(self.username, self.passwd)

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age=age

    @classmethod
    def test(cls):
        print("cls method")
    
    @staticmethod
    def teststatic():
        print(User.name) #通过类名访问类属性
        print("cls method")

u=User("mail", "test")
print(u.name)
u.name="newname"
print(u.name)
print(User.name)

User.name="dd"
print(User.name)
del u.name
print(u.name)
u.age=1
print(u.age)

u.dynname="testdyn"
print(u.dynname)

def dynfunc():
    print("dynfunc")
    
u.dynfunc=dynfunc
u.dynfunc()


def dynfunc1(self):
    print("dynfunc1")
    
import types
u.dynfunc1=types.MethodType(dynfunc1, User)
u.dynfunc1()

@classmethod
def classfunc(cls):
    print("cls dync func")
    
User.clsfunc=classfunc
User.clsfunc()


@staticmethod
def staticfunc():
    print("static dyn func")
    
User.staticfunc=staticfunc
User.staticfunc()


#class Student(object):
#    __slots__=("name", "age")
#
#stu=Student()
#stu.sex="male"


class CalableClass(object):
    def __call__(self):
        print("call me")
        
call=CalableClass()
call()


#类装饰器
class DecoratorClass(object):
    def __init__(self, func):
        print("---init---")
        print("func name is %s " % func.__name__)
        self.__func=func
    
    def __call__(self):
        print("---decorator func---")
        self.__func()
        
        
@DecoratorClass  #生成DecoratorClass的一个对象，所以会调用__init__方法，并且把下面装饰的函数作为参数传入
def test():
    print("---test---")
    
test()


