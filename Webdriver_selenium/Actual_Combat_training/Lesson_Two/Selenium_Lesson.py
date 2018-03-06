# coding=utf-8

from selenium import webdriver
import unittest, time


class Lesson(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.ul = 'https://jinshuju.net/f/kRXoEv'
        self.dr.get(self.ul)

    def test_demo(self):
        dr = self.dr
        elements = dr.find_elements_by_tag_name('i')
        print(elements)
        for i in elements:
            print(i)
            time.sleep(5)
            if i.get_attribute('data-value') == 5:
                i.click()

    # def tearDown(self):
    #     pass




