# coding=utf-8

import requests
import json

# Python dict

payload = {
    "chen": "mr.chen",
    "request": "GetOrPost",
    "Demo": "selenium+webDriver"
}

print(type(payload))

# 转化成json 格式
data_json = json.dumps(payload).encode()
print(type(data_json))
print(data_json)
