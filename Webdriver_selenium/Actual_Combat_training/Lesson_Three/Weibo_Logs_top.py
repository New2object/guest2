# coding=utf-8

from selenium import webdriver
import time, unittest


class Weibo_Top10(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(20)
        self.url = "http://d.weibo.com/100803?cfs=&Pl_Discover_Pt6Rank__5_filter=hothtlist_type%3D1#_0"

    def test_weibo_top10(self):
        self.dr.get(self.url)
        self.dr.find_element_by_css_selector(".title W_autocut").get_attribute("href")
        laods = self.dr.find_element_by_css_selector(".info_title S_txt2 .number").get_attribute("text")
        print(laods)

    def tearDown(self):
        time.sleep(5)
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
