# coding=utf-8

import pymysql as mysql
import sys

try:
    # Get 图片文件
    fp = open("./test.jpg")
    img = fp.read
    print(img)
    fp.close()
except IOError as e:
    print("Error %d %s " % (e.args[0], e.args[1]))
    sys.exit(1)

try:
    # mysql Connect
    conn = mysql.connect(host='localhost', user='root', password='', db='test')
    cursor = conn.cursor()

    # 注意使用Binary()函数来指定存储的是二进制
    cursor.execute("INSERT INTO images SET DATA ='%s'" % mysql.Binary(img))

    # 如果DB没有设置自动Submit,这里要提交一下
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()

except mysql.Error as e:
    print("Error %d %s " % (e.args[0],e.args[1]))
    sys.exit(1)
