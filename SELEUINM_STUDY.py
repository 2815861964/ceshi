import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# implicitly_wait是selenium 提供的当find找不到元素时每隔半秒检测一次find是否找到而不是报notfind错误，最大市场为括号内参数设定
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")
ele = driver.find_element(By.CSS_SELECTOR,"[href=\"http://tieba.baidu.com/\"]")
ele.click()
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(driver.title)
time.sleep(10)