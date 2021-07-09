import json

f = open("./xu列话.txt","w",encoding="utf-8")
#f.write(["name","age","sex"])
a = ["name","age","sex","city"]
x = json.dumps(a)  #是将数据转换为字符串
#f.write()
print(x)


#json.dumps() 将数据转换为json字符串，不会写入到文件里
#json.dump() 将数据转换为json字符串，并会写入到文件里

json.dump({"naem":"jin","age":11,"sex":"naem"},f)
 

 #loads :将json字符串加载成为python里的数据
 #load：将读取的内容加载成为pyhon里的数据

#load读取一个文件，并把文件里的内容加载成为一个对象
rf = open("./xu列话.txt","r",encoding="utf8")
p = json.load(rf)
print(p,type(p))
