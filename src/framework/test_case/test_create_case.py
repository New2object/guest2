# coding=utf-8

import unittest
from selenium import webdriver
from guest2.framework.page.login_page import LoginPage
from guest2.framework.page.Edit_post_page import EditPostPage
from guest2.framework.page.post_list_page import PostListPage
import time


class CreatePostCase(unittest.TestCase):
    def setUp(self):  # 每个TestCase之前执行
        print('before test')
        self.dr = webdriver.Chrome()

    def test_create_post_success(self):
        # arrange
        username = 'admin'
        password = 'admin123'
        title = 'test_title %s' % (str(time.time()))
        content = 'test_content_is_mr.chen'

        # act
        login_page = LoginPage(self.dr, 'wp-login.php')
        login_page.login(username, password)
        create_post_page = EditPostPage(self.dr, 'wp-admin/post-new.php')
        create_post_page.create_post(title, content)

        # assert
        post_list_page = PostListPage(self.dr, 'wp-admin/edit.php')
        self.assertTrue(title, post_list_page.first_post.text)

    def tearDown(self):  # 每个TestCase执行之后
        print('after every test')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
