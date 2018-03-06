# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest, time


class Registration(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.url = "https://jinshuju.net/f/kl2yl3"

    def testFillRegistrationTable(self):
        self.get_url = self.dr.get(self.url)
        self.dr.find_element_by_css_selector("#entry_field_1").send_keys("a794281962")
        self.dr.find_element_by_css_selector("#entry_field_2").send_keys(u"陈煜燊")
        self.dr.find_element_by_css_selector("#entry_field_3").send_keys("18898666222")
        self.dr.find_element_by_css_selector("#entry_field_4").send_keys("a794382922@qq.com")
        self.dr.find_element_by_css_selector("#entry_field_5").send_keys("0")
        province_select = Select(self.dr.find_element_by_css_selector("#entry_field_6_province"))
        province_select.select_by_value(u'广东省')
        city_select = Select(self.dr.find_element_by_css_selector("#entry_field_6_city"))
        city_select.select_by_value(u"深圳市")
        district_select = Select(self.dr.find_element_by_css_selector("#entry_field_6_district"))
        district_select.select_by_value(u"福田区")
        self.dr.find_element_by_css_selector(".fixed-width-control").send_keys(u"天权路坠龙阁")
        time.sleep(2)
        self.dr.find_element_by_css_selector(".selected-icon").click()
        self.dr.find_element_by_css_selector("#entry_field_9").send_keys(u"乙醇授课的练习")
        self.dr.find_element_by_css_selector("input[name='commit']").click()
        time.sleep(5)
        self.AssertEqual_success = self.dr.find_element_by_css_selector(".message").text
        self.assertEqual("提交成功", self.AssertEqual_success)


if __name__ == '__main__':
    unittest.main()
