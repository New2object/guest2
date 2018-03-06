# coding=utf-8

import unittest


class Login_action(unittest.TestCase):
    def login_data_success(self, username, password):
        self.dr.find_element_by_id("user_login").send_keys(username)
        self.dr.find_element_by_id("user_pass").send_keys(password)
        self.dr.find_element_by_id("wp-submit").click()


if __name__ == '__main__':
    unittest.main()
