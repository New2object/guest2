# coding=utf-8
from selenium import webdriver
import unittest, time
from parameterized import parameterized


class Word_login_Success(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.base_url = 'http://localhost/wordpress/wp-login.php'
        self.dr.get(self.base_url)
        self.dr.implicitly_wait(20)
        print('===============================Begin Test2=============================')

    def tearDown(self):
        print('=================================End Test2=============================')
        self.dr.quit()

    @parameterized.expand([
        ('用户名成功', 6, 'admin', 'admin123', ''),
    ]
    )
    def test_login_success(self, names, ID, Key, Values, Tips):
        self.dr.find_element_by_id("user_login").send_keys(u"admin")
        self.dr.find_element_by_id("user_pass").send_keys("admin123")
        self.dr.find_element_by_id("wp-submit").click()
        time.sleep(5)
        Tip = self.dr.find_element_by_id("wp-admin-bar-my-account").text
        self.assertEqual(Tip, Tips)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
