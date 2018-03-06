# coding: utf-8
import unittest
# import BSTestRunner
from selenium import webdriver  # selenium1 rc | selenium2 = webdriver + rc | selenium3
from selenium.webdriver.common.action_chains import ActionChains
from urlparse import urlparse, parse_qs
import time
from Webdriver_selenium.src.po.page.login_page import LoginPage
from Webdriver_selenium.src.po.page.dashboard_page import DashboardPage


class LoginCase(unittest.TestCase):
    def setUp(self):  # 每个用例执行之前执行
        print('before test')
        self.dr = webdriver.Firefox()
        # self.dr.get('http://139.199.192.100:8000/wp-login.php')

    def test_login_success(self):
        # def login_success(self):
        username = password = 'admin'
        login_page = LoginPage(self.dr, 'http://139.199.192.100:8000/wp-login.php')
        dashboard_page = login_page.login(username, password)

        self.assertTrue('wp-admin' in self.dr.current_url)
        self.assertTrue(username in dashboard_page.greeting_link.text)

    # def test_create_post_success(self):
    def create_post_success(self):
        # arrange
        username = password = 'admin'
        title = 'testt_title %s' % (str(time.time()))
        content = 'test_content'

        # action
        self.login(username, password)
        self.dr.get('http://139.199.192.100:8000/wp-admin/post-new.php')
        self.by_name('post_title').send_keys(title)
        self.set_content(content)
        self.by_name('publish').click()

        # assert
        self.dr.get('http://139.199.192.100:8000/wp-admin/edit.php')
        self.assertEqual(self.by_css('.row-title').text, title)

    def set_content(self, content):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '%s'" % (content)
        self.dr.execute_script(js)

    # def test_create_tag_success(self):
    def create_tag_success(self):
        # arrange
        username = password = 'admin'
        tag_name = 'tag%s' % (time.time())

        # action
        self.login(username, password)
        self.create_tag(tag_name)

        # assert
        table = self.by_id('the-list')
        create_successfully = True
        try:
            new_tag_link = table.find_element_by_link_text(tag_name)
        except:
            create_successfully = False
        self.assertTrue(create_successfully)

    # def test_delete_tag_success(self):
    def delete_tag_success(self):
        # arrange
        username = password = 'admin'
        tag_name = 'tag%s' % (time.time())

        # action
        self.login(username, password)
        tag_id = self.create_tag_and_return_tag_id(tag_name)
        self.delete_tag(tag_name, tag_id)

        # assert
        delete_success = False
        try:
            table = self.by_id('the-list')
            table.find_element_by_link_text(tag_name)
        except:
            delete_success = True

        self.assertTrue(delete_success)

    def create_tag(self, tag_name):
        self.dr.get('http://139.199.192.100:8000/wp-admin/edit-tags.php')
        self.by_id('tag-name').send_keys(tag_name)
        time.sleep(1)
        # self.by_id('submit').click()
        # 点击有时候会报错，改用js
        js = "document.querySelectorAll('#submit')[0].click()"
        self.dr.execute_script(js)
        time.sleep(1)

    def create_tag_and_return_tag_id(self, tag_name):
        self.create_tag(tag_name)
        new_tag_link = self.by_id('the-list').find_element_by_link_text(tag_name)
        href = new_tag_link.get_attribute('href')
        return self.get_tag_id_from_url(href)

    def get_tag_id_from_url(self, url):
        out = urlparse(url)
        res = parse_qs(out.query)
        print(res['tag_ID'])
        return res['tag_ID'][0]

    def delete_tag(self, tag_name, tag_id):
        self.dr.get('http://139.199.192.100:8000/wp-admin/edit-tags.php')
        self.disable_confirm()
        new_tag_link = self.by_id('the-list').find_element_by_link_text(tag_name)
        ActionChains(self.dr).move_to_element(new_tag_link).perform()
        self.by_id('tag-%s' % (tag_id)).find_element_by_css_selector('.delete').click()
        time.sleep(2)

    def disable_confirm(self):
        js = 'window.confirm=function(msg){console.log(msg);return true;};'
        # js = 'window.alert=function(msg){console.log(msg);return true;};'
        self.dr.execute_script(js)

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def by_name(self, name):
        return self.dr.find_element_by_name(name)

    def tearDown(self):  # 每个用例执行之后
        print('after every test')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
    # BSTestRunner.main()
