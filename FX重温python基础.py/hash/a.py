import hashlib
import uuid
import hmac


#这两个模块都是用来进行加密
#hashlib 有两种加密方式, md5 , sha

x = hashlib.md5() #创建一个md5对象
x.update('123456'.encode("utf-8"))  #对二进制进行加密
print(x.hexdigest())


#文件md5




#sha加密
x = hashlib.sha1("123456".encode("utf-8")) #
print(x.hexdigest())
x = hashlib.sha224("123456".encode("utf-8"))  #224位，一个16进制为4位
print(x.hexdigest())
x = hashlib.sha256("123456".encode("utf-8"))
print(x.hexdigest())
x = hashlib.sha384("123456".encode("utf-8"))
print(x.hexdigest())



#hmac加密，可以指定使用密钥进行加密
#x = hmac.new('jin'.encode("utf-8"),'weiguang'.encode("utf-8"))  #前面的jin为密钥，后面的weiguang是加密的数据
#print(x.hexdigest())



#uuid生成唯一值
x = uuid.uuid1()
print(x)
#x = uuid.uuid3()
print(x)
x = uuid.uuid4()
print(x)
