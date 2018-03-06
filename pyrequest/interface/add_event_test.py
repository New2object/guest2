import unittest
import requests
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0, parentdir)
from pyrequest.db_fixture import test_data
from parameterized import parameterized
import time, hashlib

'''
class AddEventTest(unittest.TestCase):
    # 添加发布会

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        # 发布会所有参数为空
        ("all_null", "", "", "", "", "", 10021, "parameter error"),

        # 发布会id已经存在
        ("eid_exist", 1, "一加4发布会", 2000, "深圳宝体", '2017', 10022, "event id already exists"),

        # 发布会name已经存在
        ("name_exist", 11, "红米Pro发布会", 2000, "北京水立方", '2017', 10023, "event name already exists"),

        # 发布会日期格式错误
        ("time_type_error", 11, "一加4手机发布会", 2000, "北京水立方", "2017", 10024, "start_time format error. It must be in YYYY-MM-DD HH:MM:SS format."),

        # 添加发布会成功
        ("success", 11, "一加4手机发布会", 2000, "北京水立方", "2017-06-01 12:00:00", 200, 'add event success'),

    ])
    def test_add_event_case(self, names, eid, name, limit, address, start_time, status, message):
        # 测试添加发布会所有可能场景:
        payload = {'eid': eid, 'name': name, 'limit': limit, 'address': address, 'start_time': start_time}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
'''


class AddEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_add_event"
        # app_key
        self.app_key = "&Guest-Bugmaster"
        # 当前时间
        now_time = time.time()
        self.client_time = str(now_time).split('.')[0]
        # sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.app_key
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_sign_null(self):
        '''签名参数为空'''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '',
                   'time': '', 'sign': ''}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'user sign null')

    def test_add_event_time_out(self):
        '''请求超时'''
        now_time = str(int(self.client_time) - 61)
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '',
                   'time': now_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user sign timeout')

    def test_add_event_sign_error(self):
        '''签名错误'''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '',
                   'time': self.client_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10013)
        self.assertEqual(result['message'], 'user sign error')

    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid': 11, 'name': '一加4手机发布会', 'limit': '1999', 'address': '深圳宝体中心',
                   'start_time': '2017-07-01 12:00:00',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'add event success')


'''
    def test_add_event_eid_exist(self):
        # id已经存在
        payload = {'eid': 1, 'name': '一加4发布会', 'limit': 2000,
                   'address': '深圳宝体', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        # 名称已经存在
        payload = {'eid': 11, 'name': '红米Pro发布会', 'limit': 2000,
                   'address': '北京水立方', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_time_type_error(self):
        # 日期格式错误
        payload = {'eid': 11, 'name': '一加4手机发布会', 'limit': 2000,
                   'address': '北京水立方', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])

    def test_add_event_success(self):
        # 添加成功
        payload = {'eid': 11, 'name': '一加4手机发布会', 'limit': 2000,
                   'address': "北京水立方", 'start_time': '2017-06-01 12:00:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')
'''
if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
