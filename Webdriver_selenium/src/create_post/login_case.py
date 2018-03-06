# coding: utf-8
import unittest
from selenium import webdriver
import time


class LoginCase(unittest.TestCase):
    def setUp(self):  # 每个用例执行之前执行
        print
        'before test'
        self.dr = webdriver.Firefox()
        self.dr.get('http://localhost/wordpress/wp-login.php')

    # def test_login(self):
    #     user_name = password = 'admin'
    #     self.login(user_name, password)
    #
    #     self.assertTrue('wp-admin' in self.dr.current_url)
    #     greeting_link = self.by_css('#wp-admin-bar-my-account .ab-item')
    #     self.assertTrue(user_name in greeting_link.text)

    def test_create_post(self):
        self.login_as_admin()

        self.dr.get('http://localhost/wordpress/wp-admin/post-new.php')
        title = 'This is my post for py se 10 %s' % (time.time())
        self.by_id('title').send_keys(title)
        self.set_content('post body')
        self.by_id('publish').click()

        self.dr.get('http://localhost/wordpress/wp-admin/edit.php')
        new_post_title = self.by_css('.row-title').text
        self.assertTrue(new_post_title == title)

    def set_content(self, text):
        js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' % (text)
        print(js)
        self.dr.execute_script(js)

    def login(self, user_name, password):
        self.by_id('user_login').send_keys(user_name)
        self.by_id('user_pass').send_keys(password)
        self.by_id('wp-submit').click()

    def login_as_admin(self):
        user_name = password = 'admin'
        self.login(user_name, password)

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def by_name(self, name):
        return self.dr.find_element_by_name(name)

    def tearDown(self):  # 每个用例执行之后
        print
        'after every test'
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
