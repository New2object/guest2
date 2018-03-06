# coding=utf-8
'''
class Host(object):

    def goodmorning(self, name):

        """Say good morning to guests"""
        return "Good morning, %s!" % name

if __name__ == '__main__':
    h = Host()
    hi = h.goodmorning('zhangsan')
    print(hi)
'''
"""
import time
# print(help(time))
print(type(time.strftime()))
"""
"""
def yun(a, b):
    '''这是加法
        a=int
        b=int
    '''
    return a+b
print(help(yun))
"""
'''
payload = {'username': 'admin', 'password': 'xiaoshen=='}
print(type(payload))
print(type(json.dumps(payload)))
'''
# app_key = 'W7v4D60'
# yu = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
# print(yu)
# print((16 - len(app_key) % 16) * str(16 - len(app_key) % 16))

from selenium import webdriver
import time


class TestDemo:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.base_url = 'http://www.baidu.com'

    def test_demo2(self, value=u'测试 selenium+webdriver'):
        self.dr = self.dr
        self.dr.get(self.base_url)
        js = (u'$("#kw").val("%s");$("#su").click()' % (value))
        # js = (u'$("#search_input").val("%s");$("#search_button").click()' %(keyword))
        self.dr.execute_script(js)
        time.sleep(8)
        self.dr.close()

