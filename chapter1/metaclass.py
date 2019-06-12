#使用type动态的创建类
#type是所有新式类的类,所有类都可以说是type创建的
#object是所有新式类的父类
def fun(self, name='DreamYoung'):
    print('Hello, ' + name)
    
Hello = type('Hello', (object,), dict(hello=fun))  # 创建Hello class

h = Hello()
h.hello()


