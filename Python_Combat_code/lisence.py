"""
生成激活码：
    1.搞限时促销,为应用生成激活码(或者优惠券)，使用Python生成200个激活码(或者优惠券),要求激活码不能重复
    2.将001题生成的200个激活码(或者优惠券)保存到Sqlite3关系型数据库中,需安装sqlite3数据库
"""
# coding=utf-8

import uuid
# uuid生成一个全局唯一的ID
import sys


class Lisence:
    def __init__(self, count):
        self.count = count

    def create(self):
        res = []
        for i in range(0, self.count):
            res.append(str(uuid.uuid4()))
        return res


# USAGE: python lisence.py 200

if __name__ == '__main__':
    # 不传入任何参数默认生成10个
    if len(sys.argv) != 2:
        count = 10
    else:
        count = int(sys.argv[-1])
    for l in Lisence(int(count)).create():
        print(l)
