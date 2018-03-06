# coding=utf-8
from selenium import webdriver

dr = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={
            "browserName": "chrome",
            "version": "",
            "platform": "ANY",
        }
)
dr.get("http://www.baidu.com")
dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("selenium")
dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/form/span[2]/input").click()
dr.quit()