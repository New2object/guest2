# coding=utf-8
from selenium import webdriver
from parameterized import parameterized
import unittest, time


class WordPress_login_action(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.base_url = 'http://localhost/wordpress/wp-login.php'
        self.dr.get(self.base_url)
        self.dr.implicitly_wait(20)
        print('===============================Begin Test=============================')

    def tearDown(self):
        print('=================================End Test=============================')
        self.dr.quit()

    # @parameterized.expand([
    #     (u'用户名错误', 1, 'abc', 'admin123', '错误：无效用户名。忘记密码？'),
    #     (u'用户名为空', 2, '', 'admin123', '错误：用户名一栏为空。'),
    #     (u'密码一栏为空', 3, 'admin', '', '错误：密码一栏为空。'),
    #     (u'用户和密码不存在', 4, 'dd', 'nmn', '错误：无效用户名。忘记密码？'),
    # ]
    # )
    # def test_wordpress_Login_Case(self, names, ID, Key, Values, Tips):
    #     self.dr.find_element_by_id("user_login").send_keys(Key)
    #     self.dr.find_element_by_id("user_pass").send_keys(Values)
    #     self.dr.find_element_by_id("wp-submit").click()
    #     IT = self.dr.find_element_by_id("login_error").text
    #     self.assertEqual(IT, Tips)
    #     time.sleep(2)

    def test_wordpress_user_null(self):
        self.dr.find_element_by_id("user_login").send_keys("")
        self.dr.find_element_by_id("user_pass").send_keys("admin123")
        self.dr.find_element_by_id("wp-submit").click()
        IT = self.dr.find_element_by_id("login_error").text
        self.assertEqual(IT, "错误：用户名一栏为空。")
        time.sleep(2)

    def test_wordpress_password_null(self):
        self.dr.find_element_by_id("user_login").send_keys("admin")
        self.dr.find_element_by_id("user_pass").send_keys("")
        self.dr.find_element_by_id("wp-submit").click()
        IT = self.dr.find_element_by_id("login_error").text
        self.assertEqual(IT, "错误：密码一栏为空。")
        time.sleep(2)

    def test_wordpress_user_error(self):
        self.dr.find_element_by_id("user_login").send_keys("admin111")
        self.dr.find_element_by_id("user_pass").send_keys("admin122")
        self.dr.find_element_by_id("wp-submit").click()
        IT = self.dr.find_element_by_id("login_error").text
        self.assertEqual(IT, "错误：无效用户名。忘记密码？")
        time.sleep(2)

    def test_wordpress_password_error(self):
        self.dr.find_element_by_id("user_login").send_keys("admin")
        self.dr.find_element_by_id("user_pass").send_keys("admin666")
        self.dr.find_element_by_id("wp-submit").click()
        IT = self.dr.find_element_by_id("login_error").text
        self.assertEqual(IT, "错误：admin 的密码不正确。忘记密码了？")
        time.sleep(2)

    def test_wordpress_user_success(self):
        self.dr.find_element_by_id("user_login").send_keys("admin")
        self.dr.find_element_by_id("user_pass").send_keys("admin123")
        self.dr.find_element_by_id("wp-submit").click()
        IT = self.dr.find_element_by_id("wp-admin-bar-my-account").text
        self.assertEqual(IT, "您好，admin")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
