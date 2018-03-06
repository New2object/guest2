# coding=utf-8

"""
ActionChains类提供的鼠标操作的常用方法:
        * perform() 执行所有ActionChains中的存储的行为
        * context_click() 右击
        * double_click() 双击
        * drag_and_drop() 拖动
        * move_to_element() 鼠标悬停
"""

from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
import time

'''
dr = webdriver.Chrome()
dr.get("http://yunpan.360.cn")

"""
    鼠标右击操作
"""
# 定位到要右击的元素
right_click = dr.find_element_by_id("xxx")

# 对定位到的元素执行鼠标右键操作
ActionChains(dr).context_click(right_click).perform()
'''

'''
"""
   鼠标悬停操作
"""
dr = webdriver.Chrome()
dr.get("http:www.baidu.com")
# 定位到要悬停的元素
above = dr.find_element_by_link_text(u"设置")

# 对定位到的元素执行悬停操作
ActionChains(dr).move_to_element(above).perform()
time.sleep(5)
dr.quit()
'''

'''
    鼠标双击操作
    double_click(on_element)方法用于模拟鼠标双击操作,用法同move_to_element
'''
'''
dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
# 定位到要悬停的元素
double_click = dr.find_element_by_link_text(u"学术")

# 对定位到的元素执行双击操作
ActionChains(dr).double_click(double_click).perform()
dr.quit()
'''
"""
'''
    鼠标推放操作
    drag_and_drop(source,target)在源元素上按下鼠标左键,然后移动到目标元素上释放
    * source: 鼠标拖动的源元素
    * target: 鼠标释放的目标元素
'''

dr = webdriver.Chrome()
dr.get("http://www.baidu.com")

# 定位元素的源位置
element = dr.find_element_by_css_selector("")

# 定位元素要移动的目标位置
target = dr.find_element_by_css_selector("")

# 执行元素的拖放操作
ActionChains(dr).drag_and_drop(element, target).perform()

dr.quit()
"""



