# coding=utf-8

from guest2.framework.page.base_page import BasePage


class PostListPage(BasePage):
    @property
    def first_post(self):
        return self.by_css('.row-title')

    @property
    def get_new_deletepage(self):
        link_page = self.by_css('.row-title').get_attribute('href')
        link_text = str((link_page).split('/', 4)[4])
        return link_text

    @property
    def delete_blog_submit(self):
        return self.by_css('#delete-action > a')

    @property
    def split_catalog_page(self):
        split_catalog_page = self.by_text_name(u'分类目录').get_attribute('href')
        get_split_catalog_page = split_catalog_page.split('/',4)[4]
        return get_split_catalog_page

    def submit_delete(self):
        self.delete_blog_submit.click()
