# coding=utf-8

# 定位一组元素 - - - - - -复选框

from selenium import webdriver
import os
import time

dr = webdriver.Chrome()
file_path = 'file://' + os.path.abspath('report_html/demo_1.html')
print(file_path)
dr.get(file_path)
'''
# 选择页面上所有的tag name 为input的元素
inputs = dr.find_elements_by_tag_name('input')

# 然后从中过滤出type为checkbox的元素,单击勾选
for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()
'''

# 通过XPath找到type==checkbox的元素
# checkboxes = dr.find_elements_by_xpath("//input[@type='checkbox']")

# 通过CSS找到type=checkbox的元素
checkboxs = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxs:
    checkbox.click()

# 打印当前页面上type为checkbox的个数
print(len(checkboxs))

# 把页面上第1个checkbox的勾给去掉
# pop默认是最后一个
dr.find_elements_by_css_selector('input[type=checkbox]').pop(0).click()


time.sleep(5)
dr.quit()