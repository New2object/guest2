# coding=utf-8

"""
百度注册:多窗口切换
"""

from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.implicitly_wait(10)
dr.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = dr.current_window_handle

dr.find_element_by_link_text(u"登录").click()
dr.find_element_by_link_text(u"立即注册").click()

# 获得当前所有打开的窗口句柄
all_handles = dr.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        dr.switch_to.window(handle)
        print("now register window!")
        dr.find_element_by_name("userName").send_keys('username')
        dr.find_element_by_name("phone").send_keys('18898317545')
        time.sleep(4)

# 进入搜索窗口
for handle in all_handles:
    if handle == sreach_windows:
        dr.switch_to.window(handle)
        print('now sreach window!')
        dr.find_element_by_id("TANGRAM__PSP_2__closeBtn").click()
        dr.find_element_by_id("kw").send_keys("selenium")
        dr.find_element_by_id("su").click()
        time.sleep(5)

dr.quit()
