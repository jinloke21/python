import pickle 

names = ["name","zhangsna","gaeg","sex"]
bs_name= pickle.dumps(names)
print(bs_name)

f = open("./pick.txt","wb")


f.write(bs_name)


pickle.dump("jin",open("./pick2.txt","wb"))
print("ok!")


dd= pickle.load(open("./pick2.txt","rb"))
print(dd)

