

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + "正在睡觉")


class Student(Person):

    def __init__(self,name,age,school):
        #子类重写父类的init方法
        #1. 父类名.__init__(self,name,age)
        #Person.__init__(self,name,age)
        #self.school = school
        #2. 使用super直接调用父类方法
        super(Student,self).__init__(name,age)
        self.school = school

    def sleep(self):
        print(self.name + "正在" + self.school + "睡觉" )


p = Student("jerry",21,"阳光中学")
print(Student.__mro__)  #先掉用自己的sleep()
p.sleep()









######################多态
print("*"*20 + "态度的使用")


class Dog():
    def work(self):
        print("狗正在工作")

class Attack_dog(Dog):
    def work(self):
        print("警犬正在工作")


class Bind_dog(Dog):
    def work(self):
        print("导盲犬正在工作")

class Drug_dog(Dog):
    def work(self):
        print("基毒犬正在工作")



class People():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #self.dog = dog

    def start(self,dog):
        print(self.name + "正在和狗工作")
        dog.work()



ad = Attack_dog()
a = People("张警官",21)
a.start(ad)

bd = Bind_dog()
a.start(bd)


dd = Drug_dog()
a.start(dd)






















