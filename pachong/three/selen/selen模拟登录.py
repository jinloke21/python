from selenium import webdriver
from lxml import etree
from selenium.webdriver import ActionChains
import time


def mian():
    web = webdriver.Chrome(executable_path="./chromedriver.exe")
    web.get("https://qzone.qq.com/")
    web.switch_to.frame("login_frame")
    div = web.find_element_by_id("switcher_plogin")
    div.click()
    user = web.find_element_by_id("u")
    pas = web.find_element_by_id("p")
    user.send_keys("")
    pas.send_keys("")
    sub = web.find_element_by_id("login_button")
    sub.click()
    #web.switch_to.frame("tcaptcha_iframe") 
    action = ActionChains(web)
    #tuo = web.find_element_by_id("tcaptcha_drag_thumb")
    tree = web.page_source
    tuo = web.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
    action.click_and_hold(tuo)
    from i in range(5):
        action.move_by_offset(14,0).perform()
        time.sleep(0.2)
    time.sleep(5)






if __name__ == "__main__":
    mian()
