from .base_page import BasePage
from .dashboard_page import DashboardPage


class LoginPage(BasePage):
    @property
    def username_text_field(self):
        return self.by_id('user_login')

    @property
    def password_text_field(self):
        return self.by_id('user_pass')

    @property
    def login_btn(self):
        return self.by_id('wp-submit')

    def login(self, username, password):
        self.username_text_field.send_keys(username)
        self.password_text_field.send_keys(password)
        self.login_btn.click()

        return DashboardPage(self.driver)
