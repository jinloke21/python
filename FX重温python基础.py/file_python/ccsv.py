import csv  #创建的文件名不能是和库名字一样，不然会报错

files = open("1.csv","w",encoding="utf8")
w = csv.writer(files)

#w.writerow(["name","age","city"])
#w.writerow(["jin","21","shanghai"])
#w.writerow(["wei","22","henan"])
#w.writerow(["name","age","fkdja"])
#w.writerow(["name","age","city"])
#w.writerow(["name","age","city"])
#w.writerow(["name","age","city"])

w.writerows([
    ["name","age","city"],
    ["jin",21,"zhenghzou"],
    ["wer",22,"hena"],
    ["guang",23,"beijing"],
    ["guo",24,"niuyue"]
    ])

files.close()

#csv读文件
print("*"*20 +"csv读文件")
#print("\n")

files = open("1.csv","r",encoding="utf-8")
r = csv.reader(files)

for date in r:
    print(date)




