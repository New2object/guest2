#encoding: utf-8
from weather import BaiduWeather
import unittest

class BaiduWeatherTest(unittest.TestCase):

	def setUp(self):
		self.baidu_weather = BaiduWeather()

	def tearDown(self):
		self.baidu_weather.quit()

	def test_get_today_weather(self):
		res = self.baidu_weather.get_today_weather()
		print res
		self.assertIsNotNone(res['temp'])
		self.assertIsNotNone(res['weather'])
		self.assertIsNotNone(res['wind'])

	def test_get_tomorrow_weather_v1(self):
		res = self.baidu_weather.get_tomorrow_weather_v1()
		print res
		self.assertIsNotNone(res['temp'])
		self.assertIsNotNone(res['weather'])
		self.assertIsNotNone(res['wind'])

	def test_get_tomorrow_weather_v2(self):
		res = self.baidu_weather.get_tomorrow_weather_v2()
		print res
		self.assertIsNotNone(res['temp'])
		self.assertIsNotNone(res['weather'])
		self.assertIsNotNone(res['wind'])


if __name__ == '__main__':
	unittest.main()
