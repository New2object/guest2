# encoding=utf-8
'''
https://movie.douban.com/cinema/nowplaying/shanghai/

•抓取豆瓣电影中的正在热映前12部电影，并按照评分排序，保存至txt文件

'''
from selenium import webdriver
import time
import os.path


class Get12HotMovieOrderByScore():
    def __init__(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(7)
        driver.get('https://movie.douban.com/cinema/nowplaying/shenzhen/')
        self.driver = driver

    # 获取前12部电影：获取电影名+评分，并按评分降序排列
    def get12movie(self):
        nowplaying_ele = self.driver.find_element_by_id('nowplaying')
        ul_ele = nowplaying_ele.find_element_by_xpath('.//div[contains(text(),"显示全部影片")]/preceding-sibling::div/ul')
        list_movie_ele = ul_ele.find_elements_by_xpath('./li')
        list_movie_ele = list_movie_ele[0:12]

        movie_list = [{i.get_attribute('data-title'): i.get_attribute('data-score')} for i in list_movie_ele]
        # 按分数从高到底排序
        movie_list.sort(key=lambda i: [value for key, value in i.items()][0], reverse=True)
        # 拆解成字符串
        content = ','.join([k + ':' + v for i in movie_list for k, v in i.items()])
        # 保存到txt
        self.save2txt(content)

    # 保存到txt
    def save2txt(self, content):
        # 定义保存路径
        now_day = time.strftime('%Y-%m-%d')
        Absolute_path = os.path.dirname(__file__)
        report_dir = Absolute_path + now_day
        if (not os.path.exists(report_dir)):
            os.makedirs(report_dir)
        now_time = time.strftime('%Y%m%d_%H%M%S')
        path = report_dir + '/' + now_time + '_movie12' + "_hot.txt"
        print(path)
        f = open(path, 'a', encoding='utf-8')
        # 保存
        f.write(content)
        f.close()


if __name__ == '__main__':
    Get12HotMovieOrderByScore().get12movie()
