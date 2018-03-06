# coding=utf-8

from multiprocessing import Process, Queue
import os, time, random


#  write Data Process执行的Code
def proc_write(q, urls):
    print('Process(%s) is waiting...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())


# Read Process执行的Code
def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)


if __name__ == '__main__':
    # 父进程Create Queue,并传给各个子进程
    q = Queue()
    proc_write1 = Process(target=proc_write(q, ['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write(q, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))

    # Start 子进程process_write,写入
    proc_write1.start()
    proc_write2.start()
    # Start子进程process_read,读取
    proc_reader.start()

    # 等待proc_write End...
    proc_write1.join()
    proc_write2.join()

    # proc_reader 进程里是死循环,无法等待其结束,只能强行中止:
    proc_reader.terminate()