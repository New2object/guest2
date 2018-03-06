# coding=utf-8
from selenium import webdriver
import unittest, time, os
import urllib.request


class TestZhihuImg(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.base_url = 'https://cn.bing.com/images/search?'

    def testGrilImg(self):
        self.dr.get(self.base_url)
        str_img = 'view=detailV2&ccid=m1B7BeDY&id=0659F25D1DDFE286457111856F50D079BC5CEC07&thid=OIP.m1B7BeDYX5vh3FEUPzZKrwDIEs&q=%E7%B2%89%E8%89%B2%E5%85%AC%E4%B8%BB%E6%B8%85%E7%BA%AF%E7%BE%8E%E5%A5%B3&simid=608035717212079366&mode=overlay&first=1'
        gril_img_url = self.base_url + str_img
        print(gril_img_url)
        self.dr.get(gril_img_url)
        print(u'开始抓取美女图片......')
        imgs_content = self.dr.find_element_by_css_selector("span > span > img").get_attribute('src')
        print(imgs_content)
        img_path = os.path.dirname(__file__)

        # time_str = time.strftime('-%yyyy-%m-%d')
        # print(time_str)
        # self.dr.save_screenshot(img_path)
        # self.dr.save_screenshot(img_path + time_str + '.png')
        now_time = time.strftime('%Y%m%d_%H%M%S')

        report_dir = img_path + now_time
        if (not os.path.exists(report_dir)):
            os.makedirs(report_dir)
        urllib.request.urlretrieve(imgs_content, report_dir + ".jpg")
        print(u'成功抓到一个大美女......w(ﾟДﾟ)w')


if __name__ == '__main__':
    unittest.main()
