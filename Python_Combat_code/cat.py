# coding=utf-8
import sys


def cat(file_path):
    for path in file_path:
        with open(path, 'rb') as f:
            # 以utf-8的编码格式解码输出文件内容,码点
            print(f.read().decode('UTF-8'))


def cat_line(file_path):
    for path in file_path:
        with open(path, 'rb') as f:
            start = 1
            for line in f.readlines():
                print("%s %s" % (start, line.decode("UTF-8")))
                start = start + 1


if __name__ == '__main__':
    files = sys.argv[1:]
    print(files)
    if '-n' in files:
        files.remove('-n')
        cat_line(files)
    else:
        cat(files)
