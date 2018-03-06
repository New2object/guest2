# coding=utf-8

from bs4 import BeautifulSoup
import bs4
import requests


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillBookList(BookList, html):
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('div', 'tab-list book-show-wrap').ul
    for li in ul.children:
        if isinstance(li, bs4.element.Tag):
            BookList.append(li.find('h3').string)


def printBookList(BookList, num):
    tple = "{0:{1}^10}"
    print(tple.format('书籍'), chr(12288))
    for i in range(num):
        print(tple.format(BookList[i], chr(12288)))


if __name__ == '__main__':
    book = []
    url = 'https://market.douban.com/book/?platform=web&channel=book_nav&page=1&page_num=20&'
    html = getHtmlText(url)
    fillBookList(book, html)
    printBookList(book, 20)
