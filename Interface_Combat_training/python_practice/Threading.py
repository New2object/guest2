# coding=utf-8
'''
1.threading 模块创建多线程
'''
'''
import random
import time, threading


# 新线程执行的代码:
def thread_run(urls):
    print('Current %s is running...' % threading.current_thread().name)
    for url in urls:
        print('%s--->>> %s' % threading.current_thread().name, url)
        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)


print('%s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1', 'url_2', 'url_3'],))
t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4', 'url_5', 'url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)
'''

# 通过从threading.Thread继承创建线程类的方式
import random,os
import threading, time


class myThead(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print('Current %s is running...' % threading.current_thread().name)
        for url in self.urls:
            print('%s --->>> %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)


print('%s is running...' % threading.current_thread().name)

t1 = myThead(name='Thread_1', urls=['url_1', 'url_2', 'url_3'])
t2 = myThead(name='Thread_2', urls=['url_4', 'url_5', 'url_6'])
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended...' % threading.current_thread().name)
