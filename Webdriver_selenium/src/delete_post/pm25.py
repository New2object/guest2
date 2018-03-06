# ecoding: utf-8
"""
抓取北上广深的pm2.5值并按照空气质量从优到劣排序
"""
from selenium import webdriver


class PM25:
    def __init__(self):
        base_url = "http://www.pm25.com/%s.html"
        self.urls = []
        for city in ['beijin', 'shanghai', 'guangzhou', 'shenzhen']:
            self.urls.append(base_url % (city))

    def __enter__(self):
        self.dr = webdriver.Firefox()
        return self

    def __exit__(self, p1, p2, p3):
        self.dr.quit()

    def get_pm25(self):
        result = []
        for url in self.urls:
            result.append(self.get_pm25_for_city(url))

        return sorted(result, key=lambda d: d['pm25'], reverse=True)

    def get_pm25_for_city(self, city_url):
        self.dr.get(city_url)
        return {
            'city': self.dr.find_element_by_class_name('bi_loaction_city').text,
            'pm25': int(self.dr.find_element_by_class_name('bi_aqiarea_num').text)
        }


if __name__ == '__main__':
    with PM25() as pm:
        print(pm.get_pm25())
