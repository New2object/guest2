# coding=utf-8
from selenium import webdriver

# 定义主机与浏览器
lists = {
    'http://192.168.190.1:4444/wd/hub': 'chrome',
    'http://192.168.190.1:5555/wd/hub': 'firefox'}

# 通过不同的浏览器执行脚本
for host, browser in lists.items():
    print(host, browser)
    dr = webdriver.Remote(
            command_executor=host,
            desired_capabilities={'platform': 'ANY',
                                  'browserName': browser,
                                  'version': '',
                                  'javascriptEnabled': True})
    dr.get("http://www.baidu.com")
    dr.find_element_by_id("kw").send_keys(browser)
    dr.find_element_by_id("su").click()
    dr.close()
