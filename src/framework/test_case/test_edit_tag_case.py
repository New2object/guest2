# coding=utf-8
from selenium import webdriver
from guest2.framework.page.login_page import LoginPage
from guest2.framework.page.edit_tag_page import EditTagPage
import unittest, time


class AddNewTag(unittest.TestCase):
    def setUp(self):  # 每个TestCase执行之前
        print('before test')
        self.dr = webdriver.Chrome()

    def test_add_new_tag(self):
        # arrange
        username = 'admin'
        password = 'admin123'
        tag_name = 'mr.chen_%s' % (time.time())
        alias_name = 'mr.chen-test_%s' % (time.time())

        # act
        login_page = LoginPage(self.dr, 'wp-login.php')
        login_page.login(username, password)
        add_tag_page = EditTagPage(self.dr, 'wp-admin/edit-tags.php?taxonomy=post_tag')
        add_tag_page.add_new_tag(tag_name, alias_name)

        # assert
        self.assertTrue(tag_name, add_tag_page.first_tag_name.text)

    def tearDown(self):  # 每个TestCase执行之后
        print('after every test')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
