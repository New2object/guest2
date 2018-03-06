# coning=utf-8

'''
显示等待
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_element_located((By.ID, "kw"))
)
"""
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
driver---Webdriver的驱动程序(IE,Chrome,FireFox等)
timeout--最长超时时间,默认以秒为单位
poll_frequency---休眠时间的间隔(步长)时间,默认为0.5秒
ignored_exceptions----超时后的异常信息,默认情况下抛NoSuchElementException异常

until()
WebDriverWait()一般由until(或until_not())方法配合使用,

until(method,message='')
调用该方法提供的驱动程序作为一个参数,直到返回值为True

until_not(method,message='')
调用该方法提供的驱动程序作为一个参数,直到返回值为False


"""


element.send_keys('slenium')
time.sleep(5)
driver.quit()

