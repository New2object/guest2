# coding=utf-8

# 输出基本用法

print('{0},{1}'.format('zhangk', 32))
print('{},{},{}'.format('mr.chen', 'boy', 25))

print('{name},{sex},{age}'.format(age=32, sex='male', name='mr.chen'))

# 格式限定式
# 它有着丰富的"格式限定符"(语法是{}中带:号),比如:

# 填充与对齐
# 填充常跟对齐一起使用
# ^,<,>分别是居中,左对齐,右对齐,后面带宽度
# :号后面带填充的字符,只能是一个字符,不指定的话默认是用空格填充,可改为中文空格

print('{:>8}'.format('mr.chen'))
print('{:0<8}'.format('mr.chen'))
print('{:a<8}'.format('chen'))
print(':p^10'.format('chen'))

# 精度与类型f
# 精度常跟类型f一起使用
print('{:.2f}'.format(31.31412))

# 其他类型
# 主要就是进制了,b,d,o,x分别是二进制,十进制,八进制,十六进制
print('{:b}'.format(15))

print('{:d}'.format(15))

print('{:o}'.format(15))

print('{:x}'.format(15))

# 用逗号还能用做金额的千位分隔符
print('{:,}'.format(123456789))