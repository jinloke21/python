from selenium import webdriver
from PIL import Image


web = webdriver.Chrome("./choromedriver.exe")
web.get("https://kyfw.12306.cn/otn/resources/login.html")
web.maximize_window() #把浏览器最大化
div =web.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a")
div.click()
#截取当前屏幕保持为a.png图片
web.save_screenshot("a.png")
#获取验证码图片的位置
img_yaz = web.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[4]/img")
#获取验证码做上方的x,y
location = img_yaz.location
print(location)
#验证码的对应长和宽
size = img_yaz.size
print(size)
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
i = Image.open("./a.png")
frame = i.crop(rangle)
frame.save("b.png")



