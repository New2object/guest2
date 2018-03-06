import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0, parentdir)
from pyrequest.db_fixture import test_data
from parameterized import parameterized


class UserSignTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/user_sign/'

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        # 测试：phone为空的嘉宾签到
        ("phone_null", 1, "", 10021, "parameter error"),

        # 测试: eid为空的嘉宾签到
        ("eid_null", "", 13511001100, 10021, "parameter error"),

        # 测试: eid不存在的嘉宾签到
        ("eid_error", 999, 13511001100, 10022, "event id null"),

        # 测试: 签到状态已关闭的发布会
        ("status_close", 3, 13511001100, 10023, "event status is not available"),

        # 测试: 签到已结束的发布会
        ("create_time_end", 4, 13511001102, 10024, "event has started"),

        # 测试: 手机号不存在的发布会签到
        ("phone_error", 1, 18818818881, 10025, "user phone null"),

        # 测试: 没有参加发布会的嘉宾签到
        ("user_not_participate", 5, 13511001100, 10026, "user did not participate in the conference"),

        # 测试: 已经参加发布会的嘉宾签到
        ("user_has_success", 1, 13511001101, 10027, "user has sign in "),

        # 测试: 嘉宾签到成功
        ("user_success", 5, 13511001102, 200, "sign success"),
    ])
    def test_sign_phone_null(self, name, eid, phone, status, message):
        # 测试嘉宾签到发布会动作所有可能场景:
        payload = {'eid': eid, 'phone': phone}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
'''
    def test_sign_eid_null(self):
        # 测试: eid为空的嘉宾签到
        payload = {'eid': '', 'phone': 13511001100}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_sign_eid_error(self):
        # 测试: eid不存在的嘉宾签到
        payload = {'eid': 999, 'phone': 13511001100}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id null')

    def test_sign_status_close(self):
        # 测试: 签到状态已关闭的发布会
        payload = {'eid': 3, 'phone': 13511001100}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event status is not available')

    def test_sign_create_time_end(self):
        # 测试: 签到已结束的发布会
        payload = {'eid': 4, 'phone': 13511001102}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'event has started')

    def test_sign_phone_error(self):
        # 测试: 手机号不存在的发布会签到
        payload = {'eid': 1, 'phone': 18818818881}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'user phone null')

    def test_sign_user_not_participate(self):
        # 测试: 没有参加发布会的嘉宾签到
        payload = {'eid': 5, 'phone': 13511001100}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'user did not participate in the conference')

    def test_sign_user_has_success(self):
        # 测试: 已经参加发布会的嘉宾签到
        payload = {'eid': 1, 'phone': 13511001101}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10027)
        self.assertEqual(self.result['message'], 'user has sign in ')

    def test_sign_user_success(self):
        # 测试: 嘉宾签到成功
        payload = {'eid': 5, 'phone': 13511001102}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'sign success')
'''
if __name__ == '__main__':
    test_data.init_data()     # 初始化接口测试数据
    unittest.main()







