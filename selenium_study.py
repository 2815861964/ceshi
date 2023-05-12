import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# implicitly_wait是selenium 提供的当find找不到元素时每隔半秒检测一次find是否找到而不是报notfind错误，最大市场为括号内参数设定
driver.implicitly_wait(10)
driver.get("http://localhost/mgr/sign.html")
a = driver.find_element(By.ID, 'password')
a.send_keys('88888888')
a = driver.find_element(By.ID, 'username')
a.send_keys('byhy')
a = driver.find_element(By.TAG_NAME, "button")
a.click()
time.sleep(3)
a = driver.find_element(By.TAG_NAME, "button")
print(a.get_attribute('outerHTML'))
print(a.get_attribute('class'))
# a[0].click()
# a = driver.find_elements(By.CLASS_NAME, 'form-control')
# a[0].send_keys("南京中医院")
# a[1].send_keys("13270255163")
# a[2].send_keys("11111")
# a = driver.find_elements(By.TAG_NAME, "button")
# time.sleep(1)
# a[1].click()
# time.sleep(500)
driver.quit()
