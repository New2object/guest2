# coding=utf-8
from selenium import webdriver
from src.framework.page.login_page import LoginPage
from src.framework.config.data import CONFIG, TEST_DATA
import unittest


class LoginCase(unittest.TestCase):
    def setUp(self):  # 每个TestCase之前执行
        print('before test')
        self.domain = CONFIG['domain']
        self.dr = webdriver.Chrome()

    def test_login_success(self):
        # arrange[əˈrendʒ]
        username = TEST_DATA['username']
        password = TEST_DATA['password']

        # act
        login_page = LoginPage(self.dr, 'wp-login.php')
        dashboard_page = login_page.login(username, password)

        # assert
        self.assertTrue('wp-admin' in self.dr.current_url)
        self.assertTrue(username in dashboard_page.greeting_link.text)

    def tearDown(self):  # 每个TestCase执行之后
        print('after every test')
        self.dr.quit()
