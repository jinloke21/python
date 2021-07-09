

class Student():
    def __init__(self,age,name):
        self.name = name
        self.age = age

    def get(self,food):
        print (self.name + "正在吃"+ food)

    @staticmethod #如果一个对象方法中没有使用到self，则可以把它定义为静态方法
    def demo():
        print("hahha")


A = Student(21,"张三")
#A.get("牛肉面")
#A.demo()

#也可以这样调用
Student.demo()
Student.get(A,"西红柿鸡蛋伴面")


#静态方法的使用
class Calcator():
    @staticmethod
    def add(a,b):
        return a+b

print(Calcator.add(4,6))







#类对象
class Teacher():
    sex = 2

    def __init__(self,name,age):
        self.age= age
        self.name= name 

    def eat(self,tea):
        print(self.name+"正在吃"+tea)


    @classmethod   #类方法只使用类中的属性，不使用方法
    #其中的有个cls参数，用来调用类的其内置属性
    def test(cls):
        print(cls.sex)


B = Teacher("语文老师",22)
B.eat("apple")
B.test()





#单例模式
print("*"*40)


class Singleton():
    __instance = None
    __is_frist = True
    def __new__(cls,*args,**kwargs):
        #申请内存创建对象，并把对象的类型设置为cls
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,name,age):
        #只有是第一次才让创建
        if self.__is_frist == True:
            self.name = name
            self.age = age
            self.__is_frist = False




A = Singleton("jin",22)
B = Singleton("guo",23)
print(A is B)
print(A.name , B.name)








