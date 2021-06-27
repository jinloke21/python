import re

ret = re.search(r"\d+","yueducishu9999")
print(ret.group())


ret = re.findall(r"\d+","python=9999,c++=5555")
print(ret)

ret = re.sub(r"\d+","0000","python=999999")
print(ret)

ret = re.sub(r"[a-z]+","0000","python=99999999")
print(ret)

ret = re.split(r":| ","jin:wei guang is:your father")
print(ret)

ret = re.match(r"<\w+><.?><.*>","<jfa><><jfaj>")
print(ret.group())

hhh="""fakfjalf
fajflafja
fjafa
fakfa"""
ret = re.match(r".*",hhh,re.S)
print(ret.group())
print("-"*15)
print("fajlkfafaefaljflaf")
ret = re.match(r"[^e]+","fajlkfafaefaljflaf")
print(ret.group())
