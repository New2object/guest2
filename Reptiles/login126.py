# coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.126.com")

print("Before login====================")

# 打印当前页面title
title = driver.title
print(title)

# 打印当前页面url
now_url = driver.current_url
print(now_url)

# 先进入frame表单
driver.switch_to.frame("x-URS-iframe")

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").clear()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys("a794281961")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").send_keys("chenyushen123")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a").click()
# driver.switch_to.default_content()
# u = driver.find_element_by_id("spnUid").text
# print(u)


# 在该页面休眠10秒
new2 = driver.current_url
print(new2)
time.sleep(10)

# 获得登录的用户名

driver.quit()
