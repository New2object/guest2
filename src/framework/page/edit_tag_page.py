# coding=utf-8
from guest2.framework.page.base_page import BasePage


class EditTagPage(BasePage):
    @property
    def first_tag_name(self):
        return self.by_css('.row-title')

    @property
    def input_add_new_tag(self):
        return self.by_css('#tag-name')

    @property
    def input_alias_name(self):
        return self.by_css('#tag-slug')

    @property
    def submit_add_new_tag(self):
        return self.by_css('.submit #submit')

    def add_new_tag(self, tag_name, alias_name):
        self.input_add_new_tag.send_keys(tag_name)
        self.input_alias_name.send_keys(alias_name)
        self.submit_add_new_tag.click()
