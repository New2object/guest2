import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0, parentdir)
from pyrequest.db_fixture import test_data
from parameterized import parameterized


class GetGuestTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/get_guest_list/'

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        # 查询eid为空的嘉宾
        ("eid_null", "", "", 10021, "eid cannot be empty"),

        # 查询eid不存在的嘉宾
        ("eid_not_exist", 999, 13511001100, 10022, "query result is empty"),

        # 根据eid和phone查询成功
        ("get_eid_phone_success", 1, 13511001100, 200, "success"),

        # 查询:eid和phone不相符合的嘉宾
        ("eid_phone_not_meet", 5, 13511001100, 10022, "query result is empty"),
    ])
    def test_get_guest_data_case(self, name, eid, phone, status, message):
        # 测试查询嘉宾动作所有可能场景:
        r = requests.get(self.base_url, params={'eid': eid, 'phone': phone})
        self.result = r.json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
'''
    def test_get_guest_eid_not_exist(self):
        # 查询eid不存在的嘉宾
        r = requests.get(self.base_url, params={'eid': 999, 'phone': 13511001100})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_guest_phone_success(self):
        # 根据eid和phone查询成功
        r = requests.get(self.base_url, params={'eid': 1, 'phone': 13511001100})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')

    def test_get_guest_eid_phone_not_meet(self):
        # 查询:eid和phone不相符合的嘉宾
        r = requests.get(self.base_url, params={'eid': '5', 'phone': 13511001100})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')
'''
if __name__ == '__main__':
    test_data.init_data()    # 初始化接口测试数据
    unittest.main()





















