# coding=utf-8
import time
import unittest

from selenium import webdriver

from guest2.framework.page.login_page import LoginPage
from guest2.framework.page.post_list_page import PostListPage
from guest2.framework.page.split_catalog_page import SplitCatalogPage


class AddSplitCatalog(unittest.TestCase):
    def setUp(self):
        print('before test...')
        self.dr = webdriver.Chrome()

    def test_add_splitcatalog(self):
        # arrange
        username = 'admin'
        password = 'admin123'
        tag_name = 'me.chen_%s' % (time.time())
        alias_name = 'alias_name_chen_%s' % (time.time())
        describe_name = 'me.chen_No.1'

        # act
        login_page = LoginPage(self.dr, 'wp-login.php')
        login_page.login(username, password)
        s_list_page = PostListPage(self.dr, 'wp-admin/edit.php')
        splict_str = s_list_page.split_catalog_page
        edit_page = SplitCatalogPage(self.dr, splict_str)
        edit_page.create_new_catalog(tag_name, alias_name, describe_name)

        # assert
        self.assertTrue(tag_name, edit_page.new_catalog_name.text)

    def tearDown(self):
        print('after evert test...')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
