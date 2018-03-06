# coding=utf-8
""""
from selenium import webdriver
import unittest

# 导入login文件
from Webdriver_selenium.Test_project.Test_case.public import login


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(30)
        self.base_url = "http://www.126.com"
        self.verificationErrors = []

    def test_login(self):
        dr = self.dr
        dr.get(self.base_url)

        # 登录
        login.login(self, "a794281961", "a123456")

        # 获取断言信息进行断言
        text = dr.find_element_by_id("spnUid").text
        self.assertEqual(text, "a794281961@126.com")

        # 调用退出函数
        login.logout(self)

    def tearDown(self):
        self.dr.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
"""""

from selenium import webdriver
import unittest
from Webdriver_selenium.Test_project.Test_case.public import login
import xml.dom.minidom

# 打开xml文档
dom = xml.dom.minidom.parse('C:\\Users\\Hasee\\guest2\\Webdriver_selenium\\Test_project\\Test_date\\login.xml')
print(dom)
# 得到文档元素对象
root = dom.documentElement
print(root)


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors = []

    def test_null(self):
        '''
        用户名,密码为空
        :return:
        '''
        dr = self.dr
        dr.get(self.base_url)
        logins = root.getElementsByTagName('null')
        # 获得null标签的username,password属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 通过firstChild.data获取登录的验证信息
        print(prompt_info)
        # 登录
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[7]/div[2]").text
        self.assertEqual(text, prompt_info)

    def test_pawd_null(self):
        '''
        输入用户名,密码为空
        :return:
        '''
        dr = self.dr
        dr.get(self.base_url)
        logins = root.getElementsByTagName("pawd_null")
        # 获得pawd_null标签的username,password属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        print(prompt_info)
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[7]/div[2]").text
        self.assertEqual(text, prompt_info)

    def test_user_null(self):
        '''
        用户名为空,只输入密码
        :return:
        '''
        dr = self.dr
        dr.get(self.base_url)
        logins = root.getElementsByTagName('user_null')
        # 获得null标签的username,password属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        print(prompt_info)
        # 登录
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[7]/div[2]").text
        self.assertEqual(text, prompt_info)

    def test_error(self):
        '''
        用户名密码错误
        :return:
        '''
        dr = self.dr
        dr.get(self.base_url)
        logins = root.getElementsByTagName('error')
        # 获得null标签的username,password属性值
        username = logins[0].getAttribute('username')
        password = logins[0].getAttribute('password')
        prompt_info = logins[0].firstChild.data
        print(prompt_info)
        print(help(logins))
        # 登录
        login.login(self, username, password)
        # 获取断言信息进行断言
        text = dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[7]/div[2]").text
        self.assertEqual(text, prompt_info)

    def tearDown(self):
        self.dr.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
