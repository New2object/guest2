# coding=utf-8

from selenium import webdriver
import unittest,time


class Weather(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.url = 'http://www.weather.com.cn/weather/101280601.shtml'
        self.dr.get(self.url)

    def send_email(self, email, content):
        pass

    def get_temperature(self):
        max_temperature = self.dr.find_element_by_css_selector("ul[class='t clearfix']>li>p[class='tem']>span").text
        print(max_temperature)
        min_temperature = self.dr.find_element_by_css_selector("ul[class='t clearfix']>li>p[class='tem']>i").text
        print(min_temperature)
        if max_temperature < '30℃' or min_temperature > '10℃':
            print('明天气温温和,温度为: %s~%s' % (min_temperature, max_temperature))
        elif min_temperature > '30℃':
            print('明天高温天气,请做好高温天气预防: %s' % (min_temperature))
        elif max_temperature < '10℃':
            print('明天低温天气,气温为: %s,请注意保暖!' % (min_temperature))
        else:
            print('BiuBiuBiu')

    def get_weather(self):
        texts = self.dr.find_element_by_css_selector("ul[class='t clearfix']>li>p[class='wea']").text
        print(texts)
        if "雨" in texts:
            print("明天有很大机率会下雨,出门请准备雨伞")
        else:
            print("明天不用打伞")

    def test_get_weather(self):
        self.get_weather()
        self.get_temperature()

    def send_notification(self, email):
        weather = self.get_weather()
        temmperature = self.get_temperature()
        content = ''

        if weather == 'raining':
          content += '明天下雨，'
        else:
          content += '明天晴天，'

        if temmperature < 10:
          content += '温度低于10度，请注意保暖'

        if temmperature > 30:
          content += '温度高于30度，请注意高温'

        self.send_email(email, content)
if __name__ == '__main__':
    unittest.main()