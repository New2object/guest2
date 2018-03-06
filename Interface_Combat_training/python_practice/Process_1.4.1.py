# coding=utf-8

'''
    import os
    
    # 第一种方式: 使用os模块中的fork方式实现多进程
    # AttributeError: module 'os' has no attribute 'fork'  -- 注: Windows系统os内核是没有fork模块的
    if __name__ == '__main__':
        print('current Process (%s) start ...' % (os.getpid()))
        pid = os.fork()
        if pid < 0:
            print('error in fork')
        elif pid == 0:
            print('I am child process (%s) and my parent process is (%s)', (os.getpid(), os.getpid()))
        else:
            print('I (%s) create a child process (%s).', (os.getpid(), pid))
'''

'''
import os
from multiprocessing import Process


# 子进程要执行的code

def run_proc(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % (os.getpid()))
    p_list = []
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        p_list.append(p)
        print('Process will start.')
        p_list[i].start()
    for p in p_list:
        p.join()
    print('Process end.')
'''

'''
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print('Task %s (pid= %s ) is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))

    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')
'''

'''
# Queue进程间通信
from multiprocessing import Process, Queue
import os, time, random


# Write data process execute the code  注:写数据进程执行的代码
def proc_write(q, urls):
    print('Process %s is writing...' % (os.getpid()))
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())


# Read data process execute the code 注: 读数据进程执行的代码
def proc_read(q):
    print('Process %s is running...' % (os.getpid()))
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)


if __name__ == '__main__':
    # Parent process[ˈpɛrənt ˈprɑsˌɛs] Create queue,并传给各个子进程
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))
    # start child proc_write,write 注:启动子进程pro_write,write
    proc_write1.start()
    proc_write2.start()
    # start child pro_reader,Reader 注: 启动子进程pro_reader,reader
    proc_reader.start()

    # Wait pro_write end... 注: 等待pro_write 结束
    proc_write1.join()
    proc_write2.join()

    # Wait pro_reader end... 注: proc_reader process里是死循环,无法等待结束,只能强行terminate终止
    proc_reader.terminate()
'''

# pipe进程间通信
import random
import os, time


def pro_send(pipe, urls):
    for url in urls:
        print('Process (%s) send: %s' % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def pro_recv(pipe):
    while True:
        print('Process (%s) rev: %s' % (os.getpid(), pipe.recv()))
        time.sleep(random.random())
