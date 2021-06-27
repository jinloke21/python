import re

html_str = "<h1>jfaljag32Afaf</h1>"
ret = re.match(r"<\w+>.+</\w+>",html_str)
print(ret.group())


# \w is not "\"
#hhh = "/"
#ret = re.match(r"\w",hhh)
#print(ret.group())

html_str2 = "<body><h1>fafjalkfja</h1></body>"
ret = re.match(r"<(\w+)><(\w+)>.+</\2></\1>",html_str2)
print(ret.group())

ret = re.match(r"<(?P<p1>\w+)><(?P<p2>\w+)>.*</(?P=p2)></(?P=p1)>",html_str2)
print(ret.group())
