import time

# 当前时间戳
now_time = time.time()
print('当前时间戳:' + str(now_time))
s = str(now_time).split('.')[0]
print(s)


# 转换成日期格式
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))
print('日期格式:' + str(otherStyleTime))