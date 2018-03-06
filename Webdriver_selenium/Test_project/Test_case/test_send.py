# coding=utf-8
from selenium import webdriver
import unittest
from Webdriver_selenium.Test_project.Test_case.public import login
import xml.dom.minidom


# 打开xml文档
dom = xml.dom.minidom.parse('C:\\Users\Hasee\guest2\Webdriver_selenium\Test_project\Test_date\login.xml')

# 得到文档元素对象
root = dom.documentElement


class TestSendMail(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors = []

    # 只填写收件人发送邮件
    def test_send_mail(self):
        dr = self.dr
        dr.get(self.base_url)
        # 登录
        login.login(self, "a794281961", "a123456")
        # 写信
        dr.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]").click()
        # 填写收件人
        dr.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys("a794281961@126.com")

        # 点击发送
        dr.find_element_by_class_name("nui-btn-text").click()

        # 点击不需写主题直接点击发送
        dr.find_element_by_css_selector("span.nui-btn-text").click()

        # 断言发送结果
        text = dr.find_element_by_class_name("tK1").text
        self.assertEqual(text, u'发送成功')
        login.logout(self)

    def tearDown(self):
        self.dr.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == '__main__':
    unittest.main()




