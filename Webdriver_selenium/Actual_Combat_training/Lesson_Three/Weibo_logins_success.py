# coding=utf-8

from selenium import webdriver
import unittest


class Login_user(unittest.TestCase):
    def login_success(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(20)
        self.url = "http://d.weibo.com"
        self.dr.get(self.url)

    def test_logins_success(self, username, password):
        self.login_success()
        self.dr.find_element_by_css_selector("#loginname").send_keys(username)
        self.dr.find_element_by_css_selector(".W_input").send_keys(password)
        self.dr.find_element_by_css_selector('span[node-type="submitStates"]').click()