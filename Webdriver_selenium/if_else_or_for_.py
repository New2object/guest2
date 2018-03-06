# coding=utf-8

'''
results = 71

if results >= 90:
    print("优秀")
elif results >= 85:
    print("良好")
elif results >= 60:
    print("一般")
else:
    print("不及格")
    '''
'''
string = "hello world"

for r in string:
    print(r)
    '''
'''
for i in range(1, 19, 2):
    print(i)
'''

'''
# 数组
shuzu = [1, 9, 2, 3, 44, 33, 2224]
print(shuzu)
print(shuzu[5])
'''

'''
# 字典
zidian = {"username": "password", 'man': 'woman', "1": "2"}

print(zidian.items())
'''

try:
    aa = '异常测试'
    print(aa)
except BaseException as msg:
    print(msg)
else:
    print('没有异常')