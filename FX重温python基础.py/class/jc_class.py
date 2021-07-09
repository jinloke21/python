


class Animal():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + "现在"+ str(self.age)+"岁了"+"正在睡觉")


class Dog(Animal):
    def bark(self):
        self.sleep()
        print(self.name+"正在叫")


class Person(Animal):
    def study(self):
        self.sleep()
        print(self.name+"正在学习")


a = Dog("大黄",23)
a.bark()

b = Person("小经",21)
b.study()








class B():
    @staticmethod
    def foo():
        print("这是B的方法")

class A():
    pass

class C(A):
    @staticmethod
    def foo():
        print("这是C的方法")

class D(B):
    pass

class X(D,C):
    pass

x = X()
x.foo()
print(X.__mro__)
    






















