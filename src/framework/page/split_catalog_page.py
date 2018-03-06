# coding=utf-8
from guest2.framework.page.base_page import BasePage
from selenium.webdriver.support.select import Select


class SplitCatalogPage(BasePage):
    @property
    def split_name(self):
        return self.by_id('tag-name')

    @property
    def alias_name(self):
        return self.by_id('tag-slug')

    @property
    def Parent_(self):
        city_select = Select(self.by_css('#parent'))
        return city_select

    @property
    def describe(self):
        return self.by_css('#tag-description')

    @property
    def click_new_catalog(self):
        return self.by_css('.submit #submit')

    @property
    def new_catalog_name(self):
        return self.by_css('.row-title')

    def create_new_catalog(self, tag_name, alias_name, describe_name):
        self.split_name.send_keys(tag_name)
        self.alias_name.send_keys(alias_name)
        self.Parent_.select_by_value('1')
        self.describe.send_keys(describe_name)
        self.click_new_catalog.click()
