# coding: utf-8

from selenium import webdriver
import selenium.webdriver.support.ui as ui


class WeatherNotification:
    def __init__(self, city):
        self.dr = webdriver.Firefox()
        self.goto_weather_page(city)

    def goto_weather_page(self, cityname):
        keyword = cityname + u'天气'
        self.dr.get('https://www.baidu.com/')
        self.dr.find_element_by_id('kw').send_keys(keyword)
        wait = ui.WebDriverWait(self.dr, 5)
        wait.until(lambda dr: dr.find_element_by_class_name('op_weather4_twoicon_container_div').is_displayed())

    @property
    def tomorrow_block(self):
        return self.dr.find_element_by_class_name('op_weather4_twoicon_day')

    def quit(self):
        self.dr.quit()

    def send_email(self, email, content):
        # atom
        print('Send email: %s' % (content))

    def get_temperature(self):
        tmp_txt = self.tomorrow_block.find_element_by_class_name('op_weather4_twoicon_temp').text
        # 28 ~ 31℃ -> 28 ~ 31 -> ['28 ', ' 31'] -> 31
        high_temp = tmp_txt.replace(u'℃', '').split('~')[-1].strip()
        return int(high_temp)

    def get_weather(self):
        wt_txt = self.tomorrow_block.find_element_by_class_name('op_weather4_twoicon_weath').text
        if u'雨' in wt_txt:
            return 'raining'
        else:
            return 'not raining'

    def send_notification(self, email):
        weather = self.get_weather()
        temmperature = self.get_temperature()

        content = ''

        if weather == 'raining':
            content += u'明天下雨，'
        else:
            content += u'明天晴天，'

        if temmperature < 10:
            content += u'温度低于10度，请注意保暖'

        if temmperature > 30:
            content += u'温度高于30度，请注意高温'

        self.quit()
        self.send_email(email, content)


if __name__ == '__main__':
    noti = WeatherNotification(u'深圳')
    noti.send_notification('me@itest.info')
