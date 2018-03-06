# coding=utf-8
import requests
'''
result = requests.get("http://www.baidu.com")
print(str(result.status_code))

if result.status_code == 200:
    print('成功')
else:
    print('失败')
print(result.cookies)
'''

r = requests.session()
url = 'http://www.baidu.com'
r.request(url,allow_redirects=True,verify=False)

