

from io import StringIO,BytesIO

stout = StringIO()

print("hello world",file=stout)
print("cao ni ma de ",file=stout)
print("ri ni ma ",file=stout)


print("读取内存缓存数据")
print(stout.getvalue())
print("读取成功!")




b_io = BytesIO()
b_io.write("内存写入二进制数据".encode("utf8"))
print(b_io.getvalue().decode("utf8"))
print("写入成功!")
