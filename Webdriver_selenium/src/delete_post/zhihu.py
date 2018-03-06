# ecoding: utf-8

"""
从zhihu.com获取每日最热和每月最热
"""

from selenium import webdriver
from datetime import date

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class Zhihu:
    def __init__(self):
        self.daily_url = 'https://www.zhihu.com/explore#daily-hot'
        self.monthly_url = 'https://www.zhihu.com/explore#monthly-hot'

    def __enter__(self):
        self.dr = webdriver.Firefox()
        return self

    def __exit__(self, p1, p2, p3):
        self.dr.quit()

    def get_daily_hots(self):
        result = []
        hots_urls = self.get_daily_hots_urls()
        for url in hots_urls:
            result.append(self.get_answer(url))
        return result

    def get_answer(self, url):
        self.dr.get(url)
        # wrap_div = self.dr.find_element_by_css_selector('.zm-item-answer.zm-item-expanded')
        article = {}
        article['question'] = self.dr.find_element_by_css_selector('#zh-question-title').text
        article['author'] = self.dr.find_element_by_css_selector('.author-link').text
        article['answer'] = self.dr.find_element_by_css_selector('.zm-editable-content.clearfix').get_attribute(
                'innerHTML')

        return article

    def get_monthly_hots(self):
        pass

    def get_daily_hots_urls(self):
        self.dr.get(self.daily_url)
        wrap_div = self.dr.find_element_by_class_name('tab-panel')
        title_url_elements = wrap_div.find_elements_by_class_name('question_link')
        assert len(title_url_elements) == 5
        urls = []
        for title in title_url_elements:
            urls.append(title.get_attribute('href'))
        return urls


class ZhihuReporter:
    def __init__(self, path):
        self.report_path = path
        self.f = open(path, 'wb')

    def write_header(self):
        self.f.write('<html><head><meta charset="utf-8">')
        self.f.write('<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css">')
        self.f.write('<title>Zhihu Report</title></head>')

    def write_body(self):
        self.f.write('<body>')

    def finish_body(self):
        self.f.write('</body>')

    def write_article(self, articles):
        self.f.write('<h3>知乎%s最热</h3>' % (date.today().strftime('%Y_%m_%d')))
        for article in articles:
            self.f.write('<div class="container">')
            article_html = '<h3>%s<small>%s</small></h3>' % (article['question'], article['author'])
            article_html += article['answer']
            self.f.write(article_html)
            self.f.write('</div>')
            self.f.write('<hr>')

    def finish_report(self):
        self.finish_body()

    self.f.write('</html>')
    self.f.close()


def build_article_report(self, articles):
    self.write_header()
    self.write_body()
    self.write_article(articles)
    self.finish_report()


if __name__ == '__main__':
    with Zhihu() as zhihu:
        articles = zhihu.get_daily_hots()
        report_name = 'zhihu_%s.html' % (date.today().strftime('%Y_%m_%d'))
        reporter = ZhihuReporter(report_name)
        reporter.build_article_report(articles)
