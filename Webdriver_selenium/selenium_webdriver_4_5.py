# coding=utf-8

"""
    键盘事件:
    有时候我们在测试时需要使用Tab键将焦点转移到下一个元素,Keys()类提供键盘上的几乎所有按键的方法,
    前面了解到send_keys()方法可以模拟键盘输入,除此之外它还可以模拟键盘上的一些组合键,例如Ctrl+C，Ctrl+A等
"""

from selenium import webdriver
# 引入Keys模块
from selenium.webdriver.common.keys import Keys
import time
dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
dr.find_element_by_id("kw").send_keys(Keys.F1)

# 输入框输入内容
dr.find_element_by_id("kw").send_keys("selenium")

# 输入框多输入的一个m
dr.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+"教程"
dr.find_element_by_id("kw").send_keys(Keys.SPACE)
dr.find_element_by_id("kw").send_keys(u"教程")

# ctrl+a 全选输入框内容
dr.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
dr.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ctrl+v 粘贴内容到输入框
dr.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 通过回车键盘来代替点击操作
dr.find_element_by_id("su").send_keys(Keys.ENTER)

time.sleep(5)
dr.quit()