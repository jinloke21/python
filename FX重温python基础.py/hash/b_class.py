

class Student():

    #用来规定只能有那些属性
    __slots__ = ('age','naem','city')


    def __init__(self,a,b):
        self.age = a
        self.naem = b

    def __eq__(self,other):
        print("eq被调用l")
        print("other是",other)

        return self.naem == other.naem and self.age == other.age





x = Student(21,"jin")
print(x.age)

#这里有个很有意思的，类中没有city属性，但这样赋值不会报错
x.city = "beijing"
print(x.city)

y = Student(21,"jin")
print(x is y)
print(x == y)

        
