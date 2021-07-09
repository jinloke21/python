



class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        self.__money = 1000

    @staticmethod
    def __test():
        print("我是Animal中的私有方法")



class Person(Animal):
    def __demo(self):
        print("我是Person中的私有方法")



p = Person("jin",21)
p._Person__demo()
#p._Person__test()
p._Animal__test()
q = Person("wei",21)
#isinstance用于判断是否是属于这个类
print(isinstance(q,Person))
print(isinstance(q,Animal))

#issubclass拥有判断一个类是不是属于其父类
print(issubclass(Person,Animal))






