from Webdriver_selenium.src.framework.page.base_page import BasePage


class EditPostPage(BasePage):
    @property
    def title_text_field(self):
        return self.by_id('title')

    @property
    def publish_btn(self):
        return self.by_name('publish')

    @property
    def permalink(self):
        return self.by_id('sample-permalink')

    def set_content(self, content):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '%s'" % (content)
        self.js(js)

    def create_post(self, title, content):
        self.title_text_field.send_keys(title)
        self.set_content(content)
        self.publish_btn.click()

    def create_post_and_return_post_id(self, title, content):
        self.create_post(title, content)
        return self.permalink.text.split('=')[-1]
