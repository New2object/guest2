# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


'''
dr = webdriver.Ie()
dr.get("http://www.baidu.com")
# 参数数字为像素点
print("设置浏览器宽480,高800显示")
dr.set_window_size(480, 800)
dr.quit()
'''

'''
# 访问百度首页
driver = webdriver.Ie()
first_url = 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

# 访问新闻页面
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

# 返回(后退)到百度首页
print("bace to %s" %(first_url))
driver.back()

# 前进到新闻页
print("forward to %s" %(second_url))
driver.forward()

# 刷新当前页面
driver.refresh()
time.sleep(5)
driver.quit()
'''

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")
time.sleep(10)
element = WebDriverWait(driver, 5, 0, 0.5).until(
        EC.presence_of_element_located((By.ID, "translateContent"))
)
element.send_keys('hello')
# driver.find_element_by_id('translateContent').send_keys('hello')
# 提交输入框的内容
driver.find_element_by_id('translateContent').submit()
time.sleep(5)
driver.quit()
