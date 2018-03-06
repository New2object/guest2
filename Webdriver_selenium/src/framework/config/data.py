import os
if os.environ['SETESTENV']:
    ENV = os.environ['SETESTENV']
else:
    ENV = 'test'

CONFIG = {
    'domain': 'http://localhost/wordpress/',
    'test': {
        'domain': 'http://localhost/wordpress/',
    },
    'production': {
        'domain': 'http://139.199.192.100:8000/'
    }
}

TEST_DATA = {
    'username': 'admin',
    'password': 'admin123'
}
