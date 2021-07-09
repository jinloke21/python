import os


a = "ewrori.dfafa"
print(a.split('.'))
print(a.partition('.'))
b = a.rpartition('.')
new_name = b[0] + ".bak." +b[2]
print(new_name)


names = os.path.splitext(a)
print(names)
