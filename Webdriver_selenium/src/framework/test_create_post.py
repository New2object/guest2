# coding: utf-8
import unittest
from selenium import webdriver  # selenium1 rc | selenium2 = webdriver + rc | selenium3
import time
from Webdriver_selenium.src.framework.page.login_page import LoginPage
from Webdriver_selenium.src.framework.page.edit_post_page import EditPostPage
from Webdriver_selenium.src.framework.page.post_list_page import PostListPage


class CreatePostCase(unittest.TestCase):
    def setUp(self):  # 每个用例执行之前执行

        self.dr = webdriver.Chrome()

    def test_create_post_success(self):
        # arrange
        username = password = 'admin'
        title = 'testt_title %s' % (str(time.time()))
        content = 'test_content'

        # action
        login_page = LoginPage(self.dr, 'wp-login.php')
        login_page.login(username, password)

        create_post_page = EditPostPage(self.dr, 'wp-admin/post-new.php')
        create_post_page.create_post(title, content)

        # assert
        post_list_page = PostListPage(self.dr, 'wp-admin/edit.php')
        self.assertEqual(title, post_list_page.first_post.text)
