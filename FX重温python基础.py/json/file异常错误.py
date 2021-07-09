
#几种常见的异常

#ZeroDivisionError:除以0的异常 1/0
#FileExistsError：文件已存在异常 os.mkdir('test')
#FileNotFoundError:文件不存在异常 open("xxx.txt")
#ValueError : int("hello")
#KeyError : person = {"name":"jin"} person["age"]
#SyntaxError: print("hello"，"good") 如使用中文逗号
#IndexError:找不的的错误 name = ["a","b","c"] print(name[10])


#自己定义异常

class Lentherror(Exception):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        print("长度必须在{}和{}之间".format(self.x,self.y))
        

passwd = input("请输入一个6到12的密码:")
x = 6
y =12 
if x<len(passwd)<y:
    print("successful!")
else:
    raise Lentherror(x,y)
