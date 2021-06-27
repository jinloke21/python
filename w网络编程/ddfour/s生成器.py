def creat_num(all_num):
    current_num = 0
    a,b = 0,1
    while current_num<all_num:
        yield a
        a,b = b,a+b
        current_num+=1


obj = creat_num(10)

for num in obj:
    print(num)
