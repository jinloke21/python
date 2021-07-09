import sys

s_in = sys.stdin

#while(True):
#    content = s_in.readline().rstrip("\n")
#    if content == "\n":
#        break
#    print(content)


sys.stdout = open("输出文件.txt","w",encoding="utf8")  #把输出内容重定向到文件
sys.stderr = open("错误输出文件","w",encoding="utf8")  #把错误的内容输出重定向文件

#while(True):
#    content = s_in.readline().rstrip("\n")  #会把\n给去除掉
#    if content == "":  #所以要把换成空
#        break
#    print(content)

我就是错误 
