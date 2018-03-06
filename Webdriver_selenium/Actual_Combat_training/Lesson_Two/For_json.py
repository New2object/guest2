import json


data = [
  {"title": "Don't cry because it's over, smile because it happened", "content": "Don't cry because it's over, smile because it happened. By Dr. Seuss"},
  {"title": "Be yourself; everyone else is already taken", "coontent": "Be yourself; everyone else is already taken. By Oscar Wilde"},
  {"title": "So many books, so little time", "content": "So many books, so little time. By  Frank Zappa"}
]
print(type(data))
# 读取json文件是用dumps方法:dumps是转换成json字符串格式
# value = json.dumps(data)
# print(type(value))
# data2 = json.loads(data)
# print(type(data2))
# loads方法是转换成list格式
for key, values in data:
    print(key, values)

# print("\"")