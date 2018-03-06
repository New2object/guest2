# encoding: utf-8
"""
登录smzdm.com并签到
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import NoSuchElementException
import time

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4'

cap = {
    'phantomjs.page.settings.userAgent': user_agent,
    "browserName": "phantomjs",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
}
dr = webdriver.PhantomJS('phantomjs', desired_capabilities=cap)
# dr = webdriver.Firefox()

dr.get('http://www.smzdm.com')
dr.find_element_by_css_selector('#sign_login .zhiyou_login').click()
time.sleep(1)

login_div = dr.find_element_by_id('pop-login-new')
assert login_div.is_displayed(), '登录框未显示'

login_frame = dr.find_element_by_id('zhiyou_login_window_iframe')
dr.switch_to.frame(login_frame)

username = 'YOUR USER NAME'
password = 'YOUR PASSWORD'

dr.find_element_by_name('username').click()
time.sleep(1)
dr.find_element_by_name('username').send_keys(username)
dr.find_element_by_name('password').click()
time.sleep(1)
dr.find_element_by_name('password').send_keys(password)
dr.find_element_by_id('login_submit').click()

time.sleep(5)

dr.switch_to.default_content()
try:
    score_btn = dr.find_element_by_class_name('signScore')
    assert score_btn.is_displayed(), '领积分按钮未显示'
    score_btn.click()
    time.sleep(3)
    assert score_btn.get_attribute('class') == 'signScored'
    print(score_btn.text)
except NoSuchElementException:
    score_btn = dr.find_element_by_class_name('signScored')
    print(score_btn.text)
