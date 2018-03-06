# coding=utf-8

from selenium import webdriver
import time

# import re
#
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
# print(re.search('runoob', 'www.runoob.com'))

# def get_cookie():
#     url = 'http://www.baidu.com'
#     dr = webdriver.Chrome()
#     dr.get(url)
#     time.sleep(2)
#     cookies = dr.get_cookies()
#     print(type(cookies))
#     print(cookies)
#     # Get list中的dict
#     print(cookies[0]['name'])
#     dr.quit()
#
#
# if __name__ == '__main__ ':
#     get_cookie()
'''
import sys
while True:
    user_number = 0
    while True:
        user_input = input("您输入的内容: '   q' to quit\n")
        if user_input.strip().lower() == 'q':
            sys.exit('Good bye....')
        if user_input.isdigit():
            user_number = int(user_input)
            break
        else:
            print('End......')
'''

'''
list = ['cat.py', 'code_stats.py', 'lisence.py', 'log.txt', 'Random_str.py']
all_codes = [f for f in list if f.split('.')[-1] == 'py']
print(all_codes)

low_list = [2, 3, 1, 7]
all_data = [f * 2 for f in low_list]
print(all_data)

l = [f for f in range(0, 10)]
all_data = [x for x in l if x % 2 == 1]
print(all_data)

b = [1, 2, 3, 4, 5]
all_data = b[:3]
all_two_data = b[3:]
all_tree_date = b[0:-1]
'''

