import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0, parentdir)
from pyrequest.db_fixture import test_data
from parameterized import parameterized


class AddGuestTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_guest/'

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        # 所有参数为空
        ("all_null", "", "", "", "", 10021, "parameter error"),

        # 发布会id-999不存在
        ("id_not_exist", 999, "alen", 13511001100, "alen@mail.com", 10022, "event id null"),

        # id为3的发布会状态未开启
        ("status_not_available", 3, "tom", 13511001102, "tom@mail.com", 10023, "event status is not available"),

        # id为2的发布会人数已上限
        ("limit_full", 2, "tom", 13511001102, "tom@mail.com", 10024, "event number is full"),

        # id为4的发布会时间已经开始
        ("time_start", 4, "tom", 13511001102, "tom@mail.com", 10025, "event has started"),

        # id为1的发布会嘉宾手机号重复
        ("phone_repeat", 1, "alen", 13511001100, "alen@mail.com", 10026, "the event guest phone number repeat"),

        # 添加嘉宾成功
        ("add_success", 1, "tom", 13511001102, "tom@mail.com", 200, "add guest success"),

    ])
    def test_add_guest_case(self, name, eid, realname, phone, email, status, message):
        # 测试添加嘉宾动作所有可能场景:
        payload = {'eid': eid, 'realname': realname, 'phone': phone, 'email': email}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
'''
    def test_add_guest_id_null(self):
        # 发布会id-999不存在
        payload = {'eid': 999, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id null')

    def test_add_guest_status_not_available(self):
        # id为3的发布会状态未开启
        payload = {'eid': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event status is not available')

    def test_add_guest_limit_full(self):
        # id为2的发布会人数已上限
        payload = {'eid': 2, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'event number is full')

    def test_add_guest_time_start(self):
        # id为4的发布会已经开始
        payload = {'eid': 4, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'event has started')

    def test_add_guest_phone_repeat(self):
        # id为1的发布会嘉宾手机号重复
        payload = {'eid': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'the event guest phone number repeat')

    def test_add_guest_success(self):
        # id为1的发布会添加嘉宾成功
        payload = {'eid': 1, 'realname': 'tom', 'phone': '13511001102', 'email': 'tom@mail.com'}
        r = requests.post(self.base_url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add guest success')
'''
if __name__ == '__main__':
    test_data.init_data()    # 初始化接口测试数据
    unittest.main()

