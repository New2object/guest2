# ecoding: utf-8
"""
获取豆瓣电影及读书中的数据
"""

from selenium import webdriver
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class Douban:
    def __init__(self):
        self.movie_url = 'https://movie.douban.com/nowplaying/shenzhen/'
        self.book_url = 'https://book.douban.com'

    def __enter__(self):
        # self.dr = webdriver.PhantomJS('phantomjs')
        self.dr = webdriver.Firefox()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.dr.quit()

    def get_current_movies(self):
        def by_rate(dic):
            return float(dic['rate'])

        self.dr.get(self.movie_url)
        self.dr.save_screenshot('douban.jpg')
        wrap_div = self.dr.find_element_by_id('nowplaying')
        cards = wrap_div.find_elements_by_class_name('list-item')
        movies = []
        for card in cards:
            item = {}
            item['name'] = card.find_element_by_css_selector('.stitle a').get_attribute('title')
            try:
                item['rate'] = card.find_element_by_css_selector('.subject-rate').text
            except:
                item['rate'] = 0

            if item['name'] and item['rate']:
                movies.append(item)

        return sorted(movies, key=by_rate, reverse=True)

    def get_hot_books(self):
        def by_rate(dic):
            return float(dic['rate'])

        self.dr.get(self.book_url)
        wrap_div = self.dr.find_element_by_css_selector('.section.popular-books')
        cards = wrap_div.find_elements_by_tag_name('li')
        books = []
        for card in cards:
            item = {}
            item['name'] = card.find_element_by_css_selector('h4.title').text
            item['rate'] = card.find_element_by_css_selector('.average-rating').text
            item['author'] = card.find_element_by_css_selector('p.author').text
            item['cagegory'] = card.find_element_by_css_selector('p.book-list-classification').text
            item['comment'] = card.find_element_by_css_selector('p.reviews').text
            if item['name'] and item['rate']:
                books.append(item)

        return sorted(books, key=by_rate, reverse=True)


class DoubanReporter:
    def __init__(self, path):
        self.report_path = path
        self.f = open(path, 'wb')

    def write_header(self):
        self.f.write('<html><head><meta charset="utf-8">')
        self.f.write('<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css">')
        self.f.write('<title>Douban Report</title></head>')

    def write_body(self):
        self.f.write('<body>')

    def finish_body(self):
        self.f.write('</body>')

    def append_image(self):
        image_name = './douban.jpg'
        self.f.write('<img src="%s" width="400px"></img>' % (image_name))

    def write_movie(self, movie_items):
        self.f.write('<h3>豆瓣正在热映</h3>')
        self.f.write('<div style="width: 400px">')
        # self.f.write('<div class="container">')
        self.f.write('<ol>')
        for movie in movie_items:
            movie_item_html = '<li>%s<span style="float:right" class="label label-primary">%s</span></li>' % (
            movie['name'], movie['rate'])
            self.f.write(movie_item_html)
        self.f.write('</ol>')
        self.f.write('</div>')

    def finish_report(self):
        self.finish_body()
        self.f.write('</html>')
        self.f.close()

    def build_movie_report(self, movie_items):
        self.write_header()
        self.write_body()
        self.write_movie(movie_items)
        self.append_image()
        self.finish_report()


if __name__ == '__main__':
    with Douban() as douban:
        movies = douban.get_current_movies()
        reporter = DoubanReporter('./movie.html')
        reporter.build_movie_report(movies)
        # print douban.get_hot_books()
