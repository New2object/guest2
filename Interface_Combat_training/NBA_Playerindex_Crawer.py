# coding=utf-8

import requests
import pandas as pd

user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers = {'User-Agent': user_agent}
url = 'http://china.nba.com/static/data/league/playerlist.json'
# 解析网页
r = requests.get(url, headers=headers).json()
num = int(len(r['payload']['players'])) - 1  # 得到list r[payload][payers]的长度
print(num)
p1_cols = []  # 用来存放p1数组的列
p2_cols = []  # 用来存放p2数组的列

#  遍历其中一个['playerProfile'],['teamProfile']:
for x in r['payload']['players'][0]['playerProfile']:
    p1_cols.append(x)

for y in r['payload']['players'][0]['playerProfile']:
    p2_cols.append(y)

p1 = pd.DataFrame(columns=p1_cols)  # 初始化一个DataFrame p1 用来存放playerProfile下的数据
p2 = pd.DataFrame(columns=p2_cols)  # 初始化一个DataFrame p2 用来存放playProfile下的数据
# 遍历一次得到一个球员的信息,分别添加到DataFrame数组中
for z in range(num):
    player = pd.DataFrame([r['payload']['players'][z]['playerProfile']])
    team = pd.DataFrame([r['payload']['players'][z]['playerProfile']])
    p1 = p1.append(player, ignore_index=True)
    p2 = p2.append(team, ignore_index=True)
p3 = pd.merge(p1, p2, left_index=True, right_index=True)  # 数据合并
p3.to_csv('f://NBA//nba_player.csv', index=False)