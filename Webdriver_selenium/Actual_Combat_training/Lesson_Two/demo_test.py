# coding=utf-8
from selenium import webdriver
import unittest, time


class Model(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get("https://www.baidu.com/")

    def by_id(self, id_key, id_vlues):
        return '$("%s").val("%s") ' % (id_key, id_vlues)

    def test_add_data(self):
        self.dr.execute_script(self.by_id("#kw", "selenium"))

    def tearDown(self):
        time.sleep(2)
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
