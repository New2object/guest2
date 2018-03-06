# coding=utf-8
'''
lists = [9, 2, 4, 7, 75, 33, 64, 1, 445]


def bubble_sort(lists):
    # 冒泡
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


print(bubble_sort(lists))
print(dir(bubble_sort(lists)))
'''

# test_str = 'This is a string'
# print(test_str.lower())
# print(test_str.upper())
# print(test_str.rstrip())

# Get dict
CONFIG = {
    'domain': 'this is a domain',
    'test': {
        'domain': 'this is a two domain'
    },
    'productions': {
        'production': 'http://www.google.com',
        'orange': u'xxx水果'
    }
}
print(CONFIG['domain'])
print(CONFIG['test']['domain'])
print(CONFIG['productions'].values())
print(CONFIG['productions']['orange'])
print(CONFIG.items())
