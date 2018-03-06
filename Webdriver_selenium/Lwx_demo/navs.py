# coding=utf-8


'''
场景:
    navs可以看作是简单的类似于tab的导航栏,一般来说导航栏都是ul+li
        先定位ul再去层级定位li中的link基本就能解决问题
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('navs.html')
print(os.path.abspath('navs.html'))
dr.get(file_path)

sleep(2)

# 方法1: 层级定位,先定位ul再定位li
dr.find_element_by_class_name('nav').find_element_by_link_text('About').click()
sleep(1)

# 方法2: 直接定位link
dr.find_element_by_link_text('Home').click()
sleep(1)

dr.quit()
