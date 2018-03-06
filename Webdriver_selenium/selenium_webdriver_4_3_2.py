# coding=utf-8

from selenium import webdriver

"""
'''
    WebElement接口常用方法:
        * size 返回元素的尺寸
        * text 获取元素的文本
        * get_attribute(name)获得属性值
        * is_displayed() # 设置该元素是否用户可见
'''
dr = webdriver.Chrome()
dr.get('http://www.youdao.com')

dr.find_element_by_id('translateContent').send_keys('hello')

# 提交输入框的内容
dr.find_element_by_id('translateContent').submit()
time.sleep(5)
dr.quit()
"""

dr = webdriver.Chrome()
dr.get("http://www.baidu.com")

# 获得输入框的尺寸
size = dr.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = dr.find_element_by_id("cp").text
print(text)

# 返回元素的属性值,可以是id,name,type或元素拥有的其它任意属性
attribute = dr.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见,返回结果为True或False
result = dr.find_element_by_id("kw").is_displayed()
print(result)

dr.quit()
