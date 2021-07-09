

class demo():
    def __enter__(self):
        print("enter方法被执行了")
        return self
    def __exit__(self,a,b,c):
        pass



#y = demo()  
#d = y.__enter__()
#print(d)

#这段代码与上面的代码效果一致
with demo() as f:
    #变量f不是demo()返回的结果，而是demo()中的__enter__(self)函数
    #返回的结果
    #并且必须含有__exit__函数
    print(f)

