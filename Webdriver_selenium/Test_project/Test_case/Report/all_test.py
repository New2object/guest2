# coding=utf-8
import unittest

# 定义测试文件查找目录

test_dir = "C:\\Users\Hasee\guest2\Webdriver_selenium\Test_project\Test_case"
testlist = unittest.defaultTestLoader.discover(test_dir,
                                               pattern='test_login.py',
                                               top_level_dir=test_dir)
print(testlist)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(testlist)