# coding=utf-8

import requests
from bs4 import BeautifulSoup


class DouPanCrawler:
    def __init__(self):
        self.url = 'http://www.book.doupan.com/'
        self.html_doc = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')

    def get_all_book(self):
        #  定义一个列表
        res = []
        for li in self.soup.find('ul', class_='list-summary').find_all('li'):
            # 定义一个字典,寻找元素中某个需要的属性
            book = {}
            # 找到title
            book['title'] = li.find('h4', class_='title').get_text()
            # 找到rating并切片空格
            book['rating'] = li.find('span', class_='average-rating').get_text().split()
            print(book)
            res.append(book)
        return res


if __name__ == '__main__':
    titles = DouPanCrawler().get_all_book()
    print(titles)
