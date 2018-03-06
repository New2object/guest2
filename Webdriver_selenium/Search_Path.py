# encoding=utf-8

import os

# 获取当前文件所在目录的上级目录
print(os.path.dirname(os.path.dirname(__file__)))

# 获取当前文件所在目录
print(os.path.dirname(__file__))

# 获取当前文件目录
print(os.getcwd())

# 获取指定目录的上级目录
print(os.path.dirname(r'c:\Users\R'))

# **************************获取相对路径
# *********************************************************************************

# 获取当前文件名称
print(os.path.basename(__file__))

# 获取指定目录的相对路径,即当前目录名: Hasee
print(os.path.basename(r'd:\Users\Hasee'))


# **************************获取绝对路径
# *********************************************************************************

# 获取当前文件的绝对路径
print(os.path.abspath(__file__))

# 获取指定目录的绝对路径
print(os.path.abspath(r'c:\Users\Hasee'))