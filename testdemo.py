# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class Testdemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.126.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_demo(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("auto-id-1496216340933").click()
        driver.find_element_by_id("auto-id-1496216340936").clear()
        driver.find_element_by_id("auto-id-1496216340936").send_keys("a123456")
        driver.find_element_by_id("dologin").click()
        driver.find_element_by_css_selector("#_mail_component_70_70 > span.oz0").click()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").clear()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys("a794281961@126.com")
        driver.find_element_by_id("_mail_toolbar_0_194").click()
        driver.find_element_by_css_selector("#_mail_button_9_221 > span.nui-btn-text").click()
        driver.find_element_by_css_selector("#_mail_button_11_249 > span.nui-btn-text").click()
        driver.find_element_by_link_text(u"退出").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

