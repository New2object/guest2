# coding: utf-8
import unittest
from selenium import webdriver  # selenium1 rc | selenium2 = webdriver + rc | selenium3
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
from Webdriver_selenium.src.framework.page.login_page import LoginPage
from Webdriver_selenium.src.framework.page.edit_post_page import EditPostPage
from Webdriver_selenium.src.framework.page.post_list_page import PostListPage


class DeletePostCase(unittest.TestCase):
    def setUp(self):  # 每个用例执行之前执行
        self.dr = webdriver.Chrome()

    def tearDown(self):  # 每个用例执行之后
        self.dr.quit()

    def test_delete_post(self):
        # arrange
        username = password = 'admin'
        title = 'testt_title %s' % (str(time.time()))
        content = 'test_content'

        # action
        # 登录
        login_page = LoginPage(self.dr, 'wp-login.php')
        login_page.login(username, password)

        # 先创建文章
        create_post_page = EditPostPage(self.dr, 'wp-admin/post-new.php')
        post_id = create_post_page.create_post_and_return_post_id(title, content)

        # 通过post id去删除文章
        post_list_page = PostListPage(self.dr, 'wp-admin/edit.php')
        post_list_page.delete_post_by_id(post_id)

        with self.assertRaises(NoSuchElementException):
            post_list_page.row_find_by_id(post_id)
