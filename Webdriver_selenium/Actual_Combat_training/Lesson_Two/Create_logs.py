import time
import unittest

from selenium import webdriver

from Webdriver_selenium.Actual_Combat_training.Lesson_Two.login_data import Login_action


class Create_data_logs(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get("http://localhost/wordpress/wp-login.php")
        self.dr.implicitly_wait(20)

    def test_create_logs_data(self):
        Login_action.login_data_success(self, "admin", "admin123")
        greeting_link = self.dr.find_element_by_css_selector("#wp-admin-bar-my-account .ab-item")
        self.assertTrue("admin" in greeting_link.text)
        time.sleep(5)
        self.create_logs()
        self.create_logs_title(u"Mr.chen")
        self.create_logs_set_content(u"这是Python实战的第二份作业")
        self.create_logs_set_content_guest()
        self.create_logs_set_content_guest_all()
        self.assertEqual("Mr.chen", self.create_logs_set_content_guest_title())

    def create_logs(self):
        return self.dr.find_element_by_link_text("撰写您的第一篇博文").click()

    def create_logs_title(self, title):
        return self.dr.find_element_by_css_selector("#titlewrap #title").send_keys(title)

    def create_logs_set_content(self, text):
        js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' % (text)
        print(js)
        self.dr.execute_script(js)

    def create_logs_set_content_guest(self):
        '''
        点击发布按钮
        :return:
        '''
        return self.dr.find_element_by_css_selector("#publishing-action #publish").click()

    def create_logs_set_content_guest_all(self):
        '''
        所有文章
        :return:
        '''
        return self.dr.find_element_by_link_text("所有文章").click()

    def create_logs_set_content_guest_title(self):
        '''
        获取当前最新文章title
        :return:
        '''
        return self.dr.find_element_by_xpath(
            "/html/body/div/div[3]/div[2]/div[1]/div[4]/form[1]/table/tbody/tr[1]/td[1]/strong/a").text


if __name__ == '__main__':
    unittest.main()
