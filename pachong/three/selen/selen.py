from selenium import webdriver
import time
chorn = webdriver.Chrome(executable_path="./chromedriver.exe")
chorn.get("www.taobao.com")
search_input = chorn.find_element_by_id("q")
search_input.send_keys("网络功防")
btn = chorn.find_element_by_class_name("btn-search")
btn.click()
time.sleep(5)
chorn.quit()
