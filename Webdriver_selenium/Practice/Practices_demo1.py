# coding=utf-8

from selenium import webdriver
import time, unittest

from Webdriver_selenium.src.po.page.base_page import BasePage
from selenium.webdriver.support.select import Select


class WordPress(unittest.TestCase, BasePage):
    def demo(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://172.16.8.76/pts/issuelist.aspx?project=442'
        self.driver.get(self.url)
        s = self.driver.find_element_by_id("ctl00_CP1_ddlFilterSuspend").find_elements_by_tag_name('option')[1]
        s.click()
