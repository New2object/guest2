import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0, parentdir)
from pyrequest.db_fixture import test_data
from parameterized import parameterized


class GetEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/get_event_list/'

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        # 发布会id和发布会名称都为空
        ("eid_name_null", "", "", 10021, "parameter error"),

        # id为999的发布会查询结果为空
        ("eid_error", 999, "", 10022, "query result is empty"),

        # 根据发布会id查询成功
        ("eid_success", 3, "", 200, "success"),

        # 根据发布会name模糊查询成功
        ("name_success", "", "红米", 200, "success"),

        # name为中华雄威的发布会查询结果为空
        ("name_error", "", "中华雄威", 10022, "query result is empty"),
    ])
    def test_get_event_data_case(self, names, eid, name, status, message):
        # 测试查询发布会动作所有可能场景:
        r = requests.get(self.base_url, params={'eid': eid, 'name': name})
        self.result = r.json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)


class GetEventListTest(unittest.TestCase):
    '''查询发布会信息(带用户认证)'''
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"
        self.auth_user = ('Username', 'admin123')

    def test_get_event_list_data_case(self):
        # auth为空
        r = requests.get(self.base_url, params={'eid': ''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10011)
        self.assertEqual(self.result['message'], 'user auth null')

    def test_get_event_list_auth_error(self):
        # auth错误
        r = requests.get(self.base_url, auth=('abc', '123'), params={'eid': ''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10012)
        self.assertEqual(self.result['message'], 'user auth fail')

    def test_get_event_list_eid_null(self):
        # eid参数为空
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid': ''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_get_event_list_eid_success(self):
        # 根据eid查询结果成功
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid': 1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['name'], u'红米Pro发布会')
        self.assertEqual(self.result['data']['address'], u'北京会展中心')





'''
    def test_get_event_eid_error(self):
        # id为999的发布会查询结果为空
        r = requests.get(self.base_url, params={'eid': 999})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_id_success(self):
        # 根据发布会id查询成功
        r = requests.get(self.base_url, params={'eid': 3})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')

    def test_get_event_name_success(self):
        # 根据发布会name模糊查询成功
        r = requests.get(self.base_url, params={'name': '红米'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')

    def test_get_event_name_error(self):
        # name为中华雄威的发布会查询结果为空
        r = requests.get(self.base_url, params={'name': '中华雄威'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')
'''
if __name__ == '__main__':
    test_data.init_data()      # 初始化接口测试数据
    unittest.main()



