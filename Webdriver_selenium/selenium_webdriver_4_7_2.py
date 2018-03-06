# coding=utf-8

from selenium import webdriver
"""
'''
隐式等待
'''

dr = webdriver.Chrome()
dr.get("http://baidu.com")
dr.implicitly_wait(10)

input_ = dr.find_element_by_id("kw22")
input_.send_keys('selenium')

dr.quit()
"""

'''
sleep
'''

from time import sleep
#
dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
sleep(2)

dr.find_element_by_id("kw").send_keys("webdriver")
dr.find_element_by_id("su").click()
sleep(3)
dr.get_screenshot_as_png("D:\\baidu.png")

dr.quit()