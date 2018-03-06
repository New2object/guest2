# coding=utf-8
# import unittest
# import requests
#
#
# class Smile_task_spi(unittest.TestCase):
#     def setUp(self):
#         self.base_url = 'http://localhost:3000/api/tasks/'
#         print('=========================Objects Start===========================')
#
#     def tearDown(self):
#         print('=========================Objects End=============================')
#
#     def test_get_user_success(self):
#         r = requests.get(self.base_url, params={'eid': 1})
#         self.result = r.json()
#         self.assertEqual(self.result['title'], 2)
#         self.assertEqual(self.result['desc'], 'Mr.chen')
#
# if __name__ == '__main__':
#     unittest.main()
import unittest
import requests
import json


class SmileTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.ip = 'http://localhost:3000'

    def test_get_all_tasks(self):
        url = self.ip + "/api/tasks/"
        response = requests.request("GET", url)

        res = response.json()
        self.assertNotEqual(res, [])
        self.assertEqual(len(res), 11)
        print(res)

    def test_post_all_tasks(self):
        url = self.ip + "/api/tasks"
        payload = {'title': 2, 'desc': u'Mr.chen'}
        response = requests.post(url, data=payload)
        self.result = response.json()
        self.assertEqual(self.result['title'], '2')
        self.assertEqual(self.result['desc'], 'Mr.chen')

    def test_put_all_tasks(self):
        puts = {'id': '2'}
        sup = json.dumps(puts)
        url = self.ip + '/api/tasks/' + sup['id']
        response = requests.put(url)
        r = response.json()
        print(r)
        self.assertEqual(r['done'], True)
        self.assertEqual(r['title'], '2')

    def test_delete_all_tasks(self):
        payload = {'id': '2'}
        url = self.ip + ' /api/tasks/' + payload['id']
        response = requests.delete(url)
        r = response.json()
        print(r)
        self.assertEqual(payload['id'], r['id'])

        # def create_data(self):


if __name__ == '__main__':
    unittest.main()
