# coding=utf-8

from guest2.framework.page.base_page import BasePage


class DashboardPage(BasePage):
    @property
    def greeting_link(self):
        return self.by_css('#wp-admin-bar-my-account .ab-item')
