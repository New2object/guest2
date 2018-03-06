# coding=utf-8

# list
# 以查字为中心向左右各扩充10个“-”字符串
print("查".center(20, '-'))

# 查找指定元素的下标
list_find = ['apple', 'banana', 'pen', 1, 2, 3]
print(list_find.index('apple'))

# 查找某元素存在的数量
print(list_find.count("apple"))

# 以增字为中心向左右各扩充10个“-”字符串
print("增".center(20, '-'))

list_add = ['apple', 'banana']
# 追加元素到末尾
list_add.append('orange')
print(list_add)

# 插入元素到指定位置
list_add.insert(1, u'苹果')
print(list_add)

print('删'.center(20, '-'))
list_del = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 从list中取出Element(删除式取出),pop可以填参数,参数为删除元素的下标
list_del.pop()
print(list_del)

# delete指定元素名的元素
list_del.remove(4)
print(list_del)

# delete对应的Element空间
del list_del[0]
print(list_del)

print("其他".center(20, '-'))
list_test4 = ['c', 'd', 'a', 'b']
list_test5 = ['1', '2', '3', '4']

# 扩展list
list_test5.extend(list_test4)
print(list_test5)

# 对list 进行排序
list_test4.sort()
print(list_test4)  # ^(*￣(oo)￣)^: py3无法对元素类型不同的进行排序

# 反转list
list_test5.reverse()
print(list_test5)

# list生成表达式
# exp = 表达式
# 过程: 1.迭代iterable中的每个元素;
# 2.每次迭代都先把结果赋值给iter_var,然后通过exp得到一个新的计算值;
# 3.最后把所有通过exp得到的计算值以一个New list的形式返回.

# [exp for iter_var in iterable]
print("1.[exp for iter_var in iterable]")
list1 = [i for i in range(10)]
print(list1)

list2 = [i * i for i in range(10, 20)]
print(list2)
print("\n")

# [exp for iter_var in iterable if_exp]
print("2.[exp for iter_var in iterable if_exp]")
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
print("\n")

# [exp for inter_var_A in iterable_A for iter_var_B in iterable_var_B]
print("3.[exp for  iter_var_A in iterable_A for iter_var_B in iterable_val_B]")
list4 = [x * y for x in range(5) for y in range(5)]
print(list4)
print("\n")

# dict

d1 = {1: "苹果", "雪碧": "雪梨"}
d1.clear()  # clear dict
print(d1)

d1 = {1: "apple", 2: "orange"}
print(d1.get(1))  # 获取dict的指定键的结果
print(d1.get(3))  # if get 不存在的key,则return None
print(d1.items())  # Get dict all the key and values
print(d1.keys())  # Get all the keys
print(d1.values())  # Get all the valus
print(d1.pop(1))  # 取出指定的下标result
print(d1.popitem())  # 不需要index alert result
print(d1)

d1 = {1: "apple", 2: "雪梨"}
d1.update({1: 'apple', 3: "pen"})  # Update result: 同键名更新,新键名则Add result
print(d1)

# Set (集合)

s1 = set(['a', 'b', 'c'])
print(s1.pop())  # 随机删除set中的某个Element,Get element return element values
print(s1)

s3 = {'a', 'b'}
s1.update(s3)  # Update
print(s1)
s1.add('f')  # Add element
print(s1)
s1.clear()  # Clear
s1 = set(['a', 'b', 'c', 'f'])
print(s1)
s1.remove('a')  # Remove目标元素,But set 如无元素,则return try
print(s1)
s1.discard('g')  # 如果set中无元素,不报错,有元素,就删除
print(s1)
b = {'a', 'g', 'b', 'd'}
print("s1.difference(b)")
print(s1.difference(b))  # 取集合s中有,b中没有的元素,并return由此元素组成的Set
print('s1.intersection(b)')
print(s1.intersection(b))  # 交集,两S和b中的交集,return s,b中都存在的元素组成的集合
print('s1.issubset()')
print(s1.issubset(b))  # 判断s是否是b的子集
print('s1.issuperset(b)')
print(s1.issuperset(b))  # 判断s是否是b的父集
print('s1.symmetric_difference(b)')
print(s1.symmetric_difference(b))  # 取差集,并创建一个New set
print('s1.union(b)')
print(s1.union(b))  # 并集
print('symmetric_difference_update')
print(s1)
print(s1.symmetric_difference_update(b))  # 无返回值
print(s1)

"""
xxxxx_update的会覆盖s1的value,如:
s1_symmetric_difference_update()
得出symmetric_difference的结果后会覆盖s1的值
"""
