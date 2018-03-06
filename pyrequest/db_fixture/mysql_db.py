# coding=utf-8
from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser

'''
# ======== Reading db_config.ini setting =========

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
'''


# ======== Mysql base operating ==========


class DB:
    def __init__(self):
        try:
            # connect to the database
            self.conn = connect(host='127.0.0.1',
                                user='root',
                                password='123456',
                                db='guest2_test',
                                port=3306,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data

    def clear(self, table_name):
        # real_sql = "truncate table" + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # insert sql statement

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        print(key)
        value = ','.join(table_data.values())
        print(value)
        real_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value + ")"

        print(real_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)

        self.conn.commit()

    # close base
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    # table_name = "sign_event"
    # data = {'id': 13, 'name': '红米发布会', '`limit`': 2000, 'status': 1,
    #         'address': '北京会展中心', 'start_time': '2017-05-08 10:45:00'}
    table_name2 = "sign_guest"
    data2 = {'realname': 'alen', 'phone': 12341234123, 'email': 'alen@mail.com',
             'sign': 0, 'event_id': 1}

    db.clear(table_name2)
    db.insert(table_name2, data2)
    db.close()

'''
修改表结构中的 创建时间字段默认值
ALTER TABLE  `sign_event` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
ALTER TABLE  `sign_guest` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
'''
