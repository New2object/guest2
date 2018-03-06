#coding: utf-8
import unittest
from selenium import webdriver
import time

class LoginCase(unittest.TestCase):

    def setUp(self): #每个用例执行之前执行
        print 'before test'
        self.dr = webdriver.Firefox()
        self.dr.get('http://localhost/wordpress/wp-login.php')

    def test_login(self):
        user_name = password = 'admin'
        self.login(user_name, password)

        self.assertTrue('wp-admin' in self.dr.current_url)
        greeting_link = self.by_css('#wp-admin-bar-my-account .ab-item')
        self.assertTrue(user_name in greeting_link.text)

    def test_login_fail_no_username_no_password(self):
        user_name = password = ''
        self.login(user_name, password)
        self.assertTrue('wp-login' in self.dr.current_url)

    def test_login_fail_correct_username_no_password(self):
        user_name = 'admin'
        password = ''
        error_msg = self.login_failed_and_return_error_msg(user_name, password)

        self.assertTrue('wp-login' in self.dr.current_url)
        self.assertEqual(error_msg, u'错误：密码一栏为空。')

    def test_login_fail_correct_username_incorrect_password(self):
        user_name = 'admin'
        password = 'incorrect'
        error_msg = self.login_failed_and_return_error_msg(user_name, password)

        self.assertTrue('wp-login' in self.dr.current_url)
        self.assertEqual(error_msg, u'错误：admin 的密码不正确。忘记密码了？')

    def test_login_fail_incorrect_username_incorrect_password(self):
        user_name = 'incorrect'
        password = 'incorrect'
        error_msg = self.login_failed_and_return_error_msg(user_name, password)

        self.assertTrue('wp-login' in self.dr.current_url)
        self.assertEqual(error_msg, u'错误：无效用户名。忘记密码？')

    def test_login_failed_data_driving(self):
        data = [
            { 'user_name': 'admin', 'password': '', 'res': u'错误：密码一栏为空。'},
            { 'user_name': 'admin', 'password': 'incorrect', 'res': u'错误：admin 的密码不正确。忘记密码了？'},
            { 'user_name': 'incorrect', 'password': 'incorrect', 'res': u'错误：无效用户名。忘记密码？'}
        ]

        for login_data in data:
            error_msg = self.login_failed_and_return_error_msg(login_data['user_name'], login_data['password'])
            self.assertTrue('wp-login' in self.dr.current_url)
            self.assertEqual(error_msg, login_data['res'], login_data['res'])

    def login(self, user_name, password):
        self.by_id('user_login').clear()
        self.by_id('user_login').send_keys(user_name)
        self.by_id('user_pass').clear()
        self.by_id('user_pass').send_keys(password)
        self.by_id('wp-submit').click()

    def login_failed_and_return_error_msg(self, user_name, password):
        self.login(user_name, password)
        return self.by_id('login_error').text

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def by_name(self, name):
        return self.dr.find_element_by_name(name)

    def tearDown(self): #每个用例执行之后
        print 'after every test'
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()
