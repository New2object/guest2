# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome()
dr.implicitly_wait(10)
url = "http://www.baidu.com"
dr.get(url=url)
# 鼠标悬停至"设置"链接
link = dr.find_element_by_link_text(u'设置')
ActionChains(dr).move_to_element(link).perform()

# 打开搜索设置
dr.find_element_by_link_text(u"搜索设置").click()

# 保存设置
dr.find_element_by_css_selector("#gxszButton > .prefpanelgo").click()
time.sleep(2)

# 接收alert
dr.switch_to_alert().accept()

dr.quit()

