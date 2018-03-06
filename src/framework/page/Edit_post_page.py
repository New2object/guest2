# coding=utf-8
from guest2.framework.page.base_page import BasePage


class EditPostPage(BasePage):
    @property
    def edit_blog_title(self):
        return self.by_name('post_title')

    def set_content(self, content):
        js = ("document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '%s'" % (content))
        return self.js(js)

    @property
    def edit_blog_submit(self):
        return self.by_id('publish')

    def create_post(self, title, content):
        self.edit_blog_title.send_keys(title)
        self.set_content(content)
        self.edit_blog_submit.click()
