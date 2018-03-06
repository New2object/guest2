import os

'''
统计代码行
'''


class CodeStats:
    def __init__(self):
        self.code_lines = 0
        self.comment_lines = 0
        self.blank_lines = 0

    def list_all_python_files(self):
        tmp = os.listdir('./')
        return [f for f in tmp if f.split('.')[-1] == 'py']

    def stats(self):
        for f in self.list_all_python_files():
            # 本来打开file默认是以GBK方法打开的,这样会有编码错误;
            # 所以这里做了小处理,是byte二进制的方式去读的,
            with open(f, 'rb') as file_handle:
                # 这里用到统计文件内容行数的方法readlines()
                for line in file_handle.readlines():
                    # 用utf-8的方式解码line file,然后再去掉空格和换行
                    striped_line = line.decode('utf-8').strip()
                    if striped_line == '':
                        self.blank_lines += 1
                    elif striped_line.startswith('#'):
                        self.comment_lines += 1
                    else:
                        self.code_lines += 1
        # 返回自身实例,以便在一个类中可以连缀调用
        return self

    def display(self):
        print("code lines: %s\ncomment lines: %s\nblank lines: %s" % (
            self.code_lines, self.comment_lines, self.blank_lines))


if __name__ == '__main__':
    CodeStats().stats().display()