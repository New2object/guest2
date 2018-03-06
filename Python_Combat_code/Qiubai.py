# coding=utf-8

import requests
from bs4 import BeautifulSoup


class QiushiBaiKe:
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/'
        self.html_doc = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')  # po ser

    def get_contents(self):
        res = []
        for content in self.soup.find_all('div', class_='content'):
            res.append(content.get_text())

        return res


if __name__ == '__main__':
    contents = QiushiBaiKe().get_contents()
    for content in contents:
        print(content)
