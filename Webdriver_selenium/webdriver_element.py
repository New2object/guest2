from selenium import webdriver
import time

driver = webdriver.Ie()
driver.get('http://192.168.121.10:38260/ich4')

driver.find_element_by_name("logon_name").send_keys("admin")
driver.find_element_by_name("passwd").send_keys("admin123")
driver.find_element_by_name("Submit").click()

time.sleep(5)

driver.close()