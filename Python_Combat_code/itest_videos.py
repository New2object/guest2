# coding:utf-8

import requests
from bs4 import BeautifulSoup


class ITestVideoWebCrawler:
    def __init__(self):
        self.url = 'http://www.itest.info/videos'
        # 通过requests.get方法请求url的html文本
        self.html_doc = requests.get(self.url).text
        # print(self.html_doc)
        # 这里用到了BeautifulSoup函数,要传两个items,第一个参数是解析哪个文本,第二个参数是用什么方法解析
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')  # 用Html驱动解析

    def get_all_titles(self):
        res = []
        # soup方法里面有两种find,一个是过滤其它元素只用一个的find方法,还有一个是用一组元素的find_all方法
        # 'a' 标签,标签中的class元素,在这里为了避免Python中的关键字,所以用了class_代替
        for a in self.soup.find_all('a', class_='video-link'):
            res.append(a.get_text())
        return res


if __name__ == '__main__':
    titles = ITestVideoWebCrawler().get_all_titles()
    print(titles)