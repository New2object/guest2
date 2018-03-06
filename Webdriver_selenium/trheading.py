# coding=utf-8

"""
    当主线程退出时，所有的子线程不论它们是否还在工作，都会被强行退出。
    有时我们并不期望这种行为，这时就引入了守护线程的概念。
    threading模块则支持守护线程。
    所以，我们直接使用 threading 来改进上面的例子
"""
import threading
from time import sleep, ctime


# 音乐播放器


def music(cys):
    for i in range(2):
        print("I was listing to %s! %s" % (cys, ctime()))
        sleep(2)

# 视频播放器


def move(cys):
    for i in range(3):
        print("I was at the %s! %s" % (ctime(), cys))
        sleep(5)


# 创造线程数组
threads = []

# 创建线程t1, 并添加到线程数组
t1 = threading.Thread(target=music, args=(u'你就不要想起我.mp3',))
threads.append(t1)

# 创建线程t2,并添加到线程数组
t2 = threading.Thread(target=move, args=(u'木乃伊.mp4',))
threads.append(t2)

if __name__ == '__main__':
    # 启动线程
    for i in threads:
        i.start()
    # 守护线程
    for i in threads:
        i.join()

    print('All end: %s' % ctime())








