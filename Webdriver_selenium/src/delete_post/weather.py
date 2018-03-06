#encoding: utf-8
"""
从baidu和http://www.weather.com.cn获取天气情况
"""

from selenium import webdriver
import time

class BaiduWeather():

	def __init__(self):
		self.query_url = 'http://www.baidu.com/s?wd=%stianqi'
		self.location = 'shenzhen'	
		self.dr = webdriver.Firefox()
		self.dr.get(self.total_url)

	@property
	def today_css_selectors(self):
		today_main_klass = '.op_weather4_twoicon_today .%s' 
		return {
			'temp': today_main_klass %('op_weather4_twoicon_temp'),
			'weather': today_main_klass %('op_weather4_twoicon_weath'),
			'wind': today_main_klass %('op_weather4_twoicon_wind'),
		}

	@property
	def tomorrow_css_selectors(self):
		tomorrow_main_klass = '.op_weather4_twoicon_day .%s' 
		return {
			'temp': tomorrow_main_klass %('op_weather4_twoicon_temp'),
			'weather': tomorrow_main_klass %('op_weather4_twoicon_weath'),
			'wind': tomorrow_main_klass %('op_weather4_twoicon_wind'),
		}

	@property
	def total_url(self):
		return self.query_url %(self.location)

	def get_weather(self, date='today'):
		if date == 'today':
			self.get_today_weather()
		elif date == 'tomorrow':
			self.get_tomorrow_weather_v1()
		else:
			raise RuntimeError('Error: unknown date')			

	def get_today_weather(self):
		return self.get_weather_by_css(self.today_css_selectors)

	@property
	def tomorrow_weather_js_hash(self):
		format = 'return $("%s").first().text().trim()'
		return {
			'temp': format %(self.tomorrow_css_selectors['temp']),
			'weather': format %(self.tomorrow_css_selectors['weather']),
			'wind': format %(self.tomorrow_css_selectors['wind']),
		}

	def get_weather_by_css(self, css_hash):
		temp = self.dr.find_element_by_css_selector(css_hash['temp']).text
		weather = self.dr.find_element_by_css_selector(css_hash['weather']).text
		wind = self.dr.find_element_by_css_selector(css_hash['wind']).text
		return {
			'temp': temp,
			'weather': weather,
			'wind': wind,
		}


	def get_tomorrow_weather_v1(self):
		return {
			'temp': self.dr.execute_script(self.tomorrow_weather_js_hash['temp']),
			'weather': self.dr.execute_script(self.tomorrow_weather_js_hash['weather']),
			'wind': self.dr.execute_script(self.tomorrow_weather_js_hash['wind']),
		}

	def get_tomorrow_weather_v2(self):
		return self.get_weather_by_css(self.tomorrow_css_selectors)

	def quit(self):
		self.dr.quit()

