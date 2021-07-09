import datetime
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __setitem__(self,key,value):
        print("set方法被调用了key={},value={}".format(key,value))
        self.__dict__[key] = value


    def __getitem__(self,item):
        return self.__dict__[item]



X = Student("jin",22)
print(X.__dict__)  #将对象装换成字典
X["name"] = "guo"  #调用[]时就会调用魔法方法__setitem__
print(X.name)

print(X['age'])  #会调用对象的getitem魔术方法



class Person():
    def __init__(self,naem,age):
        self.naem = naem 
        self.age = age 
        #设立私有属性
        self.__money = 1000

    def get_money(self):
        print("{}查询了余额".format(datetime.datetime.now()))
        return self.__money

    def set_money(self,qian):
        if type(qian)!=int:
            print("设置钱不合法1")
            return False
        self.__money = qian
        print("已经成功修改")
    def __idemo(self):
        print("成功调用私有方法!")

    def test(self):
        self.__idemo()


X = Person("张三",18)
print(X.naem,X.age)
#私有属性不可以直接拿
#print(X.__money)

#但可以通过这中形式拿取
print(X._Person__money)


#使用get和set访问私有属性
print(X.get_money())

X.set_money("hello")
X.set_money(111111)
print(X.get_money())

#同样可以设置私有函数
#X.__idemo()  #不可调用
X.test()
X._Person__idemo()  #也可以直接硬调用
