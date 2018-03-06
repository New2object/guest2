# coding=utf-8

from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get("http://www.126.com")

print("Before login================")

# 打印当前页面title
title = dr.title
print(title)

# 打印当前页面URL
now_url = dr.current_url
print(now_url)

# 执行邮箱登录
s = dr.switch_to.frame("x-URS-iframe")
dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").clear()
dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys('a794281961')
dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").send_keys('a123456')
dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a").click()
print("After login====================")
# 再次打印当前页面title
title = dr.title
print(title)

# 再次打印当前页面URL
now_url = dr.current_url
print(now_url)

# 获得登录的用户名
user = dr.find_element_by_link_text("a794281961@126.com").text
print(user)
time.sleep(5)

dr.quit()