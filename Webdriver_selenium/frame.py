# coding=utf-8

from selenium import webdriver
import time
import os
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./report_html/frame.html')
print(file_path)
dr.get(file_path)

# 先通过class_name定位到frame
xf = dr.find_element_by_class_name('nb')

# 再切换到iframe(id="if")
dr.switch_to.frame(xf)

# 下面就可以正常的操作元素了
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()

time.sleep(5)

dr.quit()