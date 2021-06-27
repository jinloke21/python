from selenium import webdriver
import time
from selenium.webdriver import ActionChains #导入动作链，用来拖动标签

def main():
    web = webdriver.Chrome(executable_path="./路径")
    web.get("https://www.baidu.com")
    #如果调用的标签存在于iframe标签中则必须通过一下操作
    web.switch_to.frame("iframe的id值") #切换浏览器作用与到iframe中
    div = web.find_element_by_id("要定位的在iframe中的标签的id值")

    #创建动作连对象,参数为浏览器对象
    action = ActionChains(web)
    #点击且长按指定的标签
    action.click_and_hold(div)

    for i range(5):
        #向右偏移17个像素，perform表示立即执行
        #参数为x水平方向，y为竖直方向
        action.move_by_offset(17,0).perform()
        time.sleep(0.5)
    action.release()
