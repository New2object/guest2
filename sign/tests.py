from django.test import TestCase
from sign.models import Event, Guest
from django.test import Client
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.


class ModelTest(TestCase):

    def setUp(self):
        # 创建两条数据(测试模板)
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=1999,
                             address='shenzhen', start_time='2017-05-03 11:25:00')
        Guest.objects.create(id=1, event_id=1, realname='alen',
                             phone='13711001101', email='alen@mail.com', sign=False)
    # 测试oneplus 3 event发布会是否成功创建,数据是否正确

    def test_event_models(self):
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    # 测试alen这位嘉宾是否已成功创建,数据是否正确

    def test_guest_models(self):
        result = Guest.objects.get(realname='alen')
        self.assertEqual(result.email, 'alen@mail.com')
        self.assertEqual(result.phone, '13711001101')
        self.assertFalse(result.sign)


class IndexPageTest(TestCase):

    '''测试index登录首页'''

    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):

    '''测试登录函数'''
    def setUp(self):
        User.objects.create_user('Admin', 'admin@mail.com', 'admin123456')
        self.c = Client()

    # 账号和密码为空
    def test_login_action_username_password_null(self):
        test_data = {'username': '', 'password': ''}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    # 账号密码错误
    def test_login_action_username_password_error(self):
        test_data = {'username': 'abc', 'password': 'abc123'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    # 登录成功
    def test_login_action_username_password_success(self):
        test_data = {'username': 'Admin', 'password': 'admin123456'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)


class EventManageTest(TestCase):

    '''发布会管理'''
    def setUp(self):
        Event.objects.create(id=2, name='xiaomi5', limit=1999, status=True,
                             address='beijing', start_time=datetime(2017, 5, 3, 15, 25, 0))
        self.c = Client()

    def test_event_manage_success(self):

        '''测试发布会:xiaomi5'''

        response = self.c.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)

    def test_event_manage_search_success(self):

        '''测试发布会搜索'''

        response = self.c.post('/event_manage/', {"name": "xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)


class GuestManageTest(TestCase):

    '''嘉宾管理'''

    def setUp(self):
        Event.objects.create(id=1, name="xiaomi5", limit=1999,
                             address='beiing', status=1, start_time=datetime(2017, 5, 3, 15, 40, 0))
        Guest.objects.create(realname="alen", phone=18811001100,
                             email='alen@mail.com', sign=0, event_id=1)
        self.c = Client()

    def test_event_manage_success(self):

        '''测试嘉宾信息:alen'''

        response = self.c.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'alen', response.content)
        self.assertIn(b'18811001100', response.content)

    def test_guest_manage_search_success(self):

        '''测试嘉宾搜索'''

        response = self.c.post('/guest_manage/', {'phone': '18811001100'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'18811001100', response.content)
        self.assertIn(b'alen@mail.com', response.content)


class SignIndexActionTest(TestCase):

    '''发布会签到'''

    def setUp(self):
        Event.objects.create(id=1, name="xiaomi5", limit=1999, address='beijing',
                             status=1, start_time='2017-5-3 16:30:00')
        Event.objects.create(id=2, name="oneplus4", limit=1998, address='shenzhen',
                             status=1, start_time='2017-7-1 16:22:22')
        Guest.objects.create(realname="alen", phone=18611001100,
                             email='alen@mail.com', sign=0, event_id=1)
        Guest.objects.create(realname="chenji", phone=13711001101,
                             email="chenji@mail.com", sign=1, event_id=2)

        self.c = Client()

    def test_sign_index_action_phone_null(self):

        '''手机号为空'''

        response = self.c.post('/sign_index_action/1/', {'phone': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error.', response.content)

    def test_sign_index_action_phone_or_event_id_error(self):

        '''手机号或者发布会ID错误'''

        response = self.c.post('/sign_index_action/2/', {'phone': 18611001100})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'event id or phone error.', response.content)

    def test_sign_index_action_user_has_sign(self):

        '''用户已签到'''

        response = self.c.post('/sign_index_action/2/', {'phone': 13711001101})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in.', response.content)

    def test_sign_index_action_sign_success(self):

        '''签到成功'''

        response = self.c.post('/sign_index_action/1/', {'phone': 18611001100})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sign in success!', response.content)
