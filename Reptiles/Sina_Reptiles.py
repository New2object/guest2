# # coding=utf-8
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
# def generate_allurl(user_in_nub):
#     url = 'http://sz.lianjia.com/zufang/xinzhou1/pg{}/'
#     for url_next in range(1, int(user_in_nub)):
#         yield url.format(url_next)
#
#
# def main():
#     user_in_nub = input('输入生成页数: ')    #
#     for i in generate_allurl(user_in_nub):
#         print(i)
#
#
# def get_allurl(generate_allurl):
#     get_url = requests.get(generate_allurl,)
#     if get_url.status_code == 200:
#         re_set = re.compile('<li.*?class="fl l-txt">.*?<a.*?class="stp.*?".*?href="(.*?)"')
#         re_get = re.findall(re_set, get_url.text)
#         print(re_get)
#
#
# if __name__ == '__main__':
#     main()
#
