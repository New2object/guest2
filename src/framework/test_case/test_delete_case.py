# coding=utf-8
import time
import unittest

from selenium import webdriver

from guest2.framework.page.Edit_post_page import EditPostPage
from guest2.framework.page.login_page import LoginPage
from guest2.framework.page.post_list_page import PostListPage


class DeleteBlogCase(unittest.TestCase):
    def setUp(self):
        print('start test delete')  # 每个测试用例之前执行
        self.dr = webdriver.Chrome()

    def test_delete_blog_success(self):
        # arrange
        username = 'admin'
        password = 'admin123'
        title = 'delete_title %s' % (str(time.time()))
        content = 'test_content_is_mr.chen'

        # act 登录页面
        login_page = LoginPage(self.dr, 'wp-login.php')
        login_page.login(username, password)

        # 编辑页面
        create_post_page = EditPostPage(self.dr, 'wp-admin/post-new.php')
        create_post_page.create_post(title, content)

        # 通过all blog list page get old page
        post_list_page = PostListPage(self.dr, 'wp-admin/edit.php')
        new_edit_page = post_list_page.get_new_deletepage
        print(new_edit_page)
        get_old_page = PostListPage(self.dr, new_edit_page)
        get_old_page.submit_delete()
        url = self.dr.current_url
        print(url)
        # assert
        post_list_page = PostListPage(self.dr, 'wp-admin/edit.php')
        self.assertIsNotNone(title, post_list_page.first_post.text)

    def tearDown(self):
        print('end test delete blog ')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
