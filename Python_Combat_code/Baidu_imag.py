# coding=utf-8
import requests, os, time, urllib
from bs4 import BeautifulSoup


class BaiDuGirl:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1462357247335_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB'
        self.html_doc = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')

    def get_all_imgs(self):
        res = []
        for imags in self.soup.find_all('img', datas_imgs='img-hover'):
            res.append(imags.get_text())
            print(u'开始抓取美女图片......')
        return res

    def Save(self):
        img_path = os.path.dirname(__file__)

        # time_str = time.strftime('-%yyyy-%m-%d')
        # print(time_str)
        # self.dr.save_screenshot(img_path)
        # self.dr.save_screenshot(img_path + time_str + '.png')
        now_time = time.strftime('%Y%m%d_%H%M%S')
        report_dir = img_path + now_time
        if (not os.path.exists(report_dir)):
            os.makedirs(report_dir)
        urllib.request.urlretrieve(img_path, report_dir + ".jpg")
        print(u'成功抓到一个大美女......w(ﾟДﾟ)w')


if __name__ == '__main__':
    titles = BaiDuGirl().get_all_imgs()
    print(titles)