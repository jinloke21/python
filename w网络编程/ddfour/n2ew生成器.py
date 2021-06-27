def creat_num(all_num):
    current_num = 0
    a,b = 0,1
    while current_num<all_num:
        ret = yield a 
        print("ret>>>>>>>>>:",ret)
        a,b = b,a+b
        current_num+=1



obj = creat_num(20)
ret = next(obj)
print(ret)

ret = obj.send("hahaha")
print(ret)
 
