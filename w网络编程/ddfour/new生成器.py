def creat_num(all_num):
    current_num = 0
    a,b = 0,1
    while current_num<all_num:
        yield a #如果函数中有yield语句法,那么is not hanshu
        a,b = b,a+b
        current_num+=1
    return "---os----"



obj = creat_num(20)
 
while 1:
    try:
        print(next(obj))
    except Exception as ret:
        print(ret.value)
        break

