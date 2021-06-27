class parent(object):
    def __init__(self,name,*args,**kwargs):
        self.name = name

class son1(parent):
    def __init__(self,name,age,*args,**kwargs):
        self.age = age


class son2(parent):
    def __init__(self,name,gender,*args,**kwargs):
        self.gender = gender


class Grandson(son1,son2):
    def __init__(self,name,age,gender):
        #super(Grandson,self).__init__(name,age,gender)
        super().__init__(name,age,gender)


print(Grandson.__mro__)

