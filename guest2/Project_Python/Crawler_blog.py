# coding=utf-8

import requests
from bs4 import BeautifulSoup
import bs4, os, time

url_list = []
headers = {
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def url_all():
    for page in range(1, 1):
        url = 'http://blog.csdn.net/?ref=toolbar_logo&page=' + str(page)
        url_list.append(url)


def essay_url():  # Search all blog address
    blog_urls = []
    for url in url_list:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.text, 'html.parser')
        for h3 in soup.find_all('h3'):
            blog_url = (h3('a')[0]['href'])
            blog_urls.append(blog_url)
    return blog_urls


def save_path():
    s_path = "F:/blog/"
    if not os.path.isdir(s_path):
        os.mkdir(s_path)
    else:
        pass

    return s_path


def save_essay(blog_urls, s_path):  # 找到所有文章,文章内容
    for url in blog_urls:
        blog_html = requests.get(url, headers=headers)
        blog_html.encoding = blog_html.apparent_encoding
        soup = BeautifulSoup(blog_html.text, 'html.parser')
        try:
            for title in soup.find('span', {"class": 'link_title'}):
                if isinstance(title, bs4.element.Tag):
                    print('------Blog title -------: ', title.text)
                    blog_name = title.text
                    blog_name = blog_name.replace("\n", '')
                    blog_name = blog_name.replace("\r", '')
                    blog_name = blog_name.replace(" ", '')
                    try:
                        file = open(s_path + str(blog_name) + '.txt', 'w')
                        file.write(str(title.text))
                        file.close()
                    except BaseException as a:
                        print(a)

            for p in soup.find('div', {"class": 'article_content'}).children:
                if isinstance(p, bs4.element.Tag):
                    try:
                        file = open(s_path + str(blog_name) + '.txt', 'a')
                        file.write(p.text)
                        file.close()
                    except BaseException as f:
                        print(f)
        except BaseException as b:
            print(b)
    print('---------------All page for end...')


time.sleep(10)
url_all()
save_essay(essay_url(), save_path())
