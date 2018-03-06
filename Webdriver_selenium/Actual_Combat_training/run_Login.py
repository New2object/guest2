# coding=utf-8

import time
from HTMLTestRunner import HTMLTestRunner
import unittest

# 指定测试用例为当前文件夹下的Actual_Combat_training目录
test_dir = 'C://Users/Hasee/guest2/Webdriver_selenium/Actual_Combat_training/Lesson_Two'
discover = unittest.defaultTestLoader.discover(test_dir,
                                               pattern='Create_logs.py')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = 'C://Users/Hasee/guest2/Webdriver_selenium/Actual_Combat_training/Report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Create WordPress Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
