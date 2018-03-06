# coding=utf-8
from time import sleep, ctime

"""
第一种:多线程
# 创建听音乐任务


def music():
    print('I was listening to music! %s' % ctime())
    sleep(2)


# 创建看电影任务
def move():
    print('I was at the movies! %s' % ctime())
    sleep(5)

if __name__ == '__main__':
    music()
    move()
    print('All end: %s' % ctime())
"""

"""
第二种: 多线程
# 音乐播放器


def music(func):
    for i in range(2):
        print('I was listening to %s! %s' % (func, ctime()))
        sleep(2)

# 视频播放器


def move(func):
    print('I was at the %s! %s' % (func, ctime()))
    sleep(5)


if __name__ == '__main__':
    music(u'爱情买卖.mp3')
    move(u'木乃伊.mp4')
    print('All end: %s' % ctime())
"""




