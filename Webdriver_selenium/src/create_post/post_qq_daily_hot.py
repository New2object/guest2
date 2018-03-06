# coding: utf-8
from selenium import webdriver


class QQDailyHot:
    def __init__(self):  # 每个用例执行之前执行
        self.dr = webdriver.Firefox()
        self.title, self.content = self.get_title_and_content_from_daily_hot()

    def get_daily_hot_url(self):
        return self.by_css('#todaytop a').get_attribute('href')

    def get_title_and_content_from_daily_hot(self):
        self.dr.get('http://www.qq.com/')
        url = self.get_daily_hot_url()
        self.dr.get(url)
        title = self.by_id('sharetitle').text
        content = self.by_id('articleContent').get_attribute('innerHTML')
        return (title, content)

    def quit(self):
        self.dr.quit()

    def create_post_from_daily_hot(self):
        self.dr.get('http://localhost/wordpress/wp-login.php')
        self.login_as_admin()

        self.dr.get('http://localhost/wordpress/wp-admin/post-new.php')

        self.by_id('title').send_keys(self.title)
        self.set_content(self.content)
        self.by_id('publish').click()

    def set_content(self, text):
        text = text.strip()
        js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML=\'%s\'' % (text)
        print(js)
        self.dr.execute_script(js)

    def login(self, user_name, password):
        self.by_id('user_login').send_keys(user_name)
        self.by_id('user_pass').send_keys(password)
        self.by_id('wp-submit').click()

    def login_as_admin(self):
        user_name = password = 'admin'
        self.login(user_name, password)

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def by_name(self, name):
        return self.dr.find_element_by_name(name)


if __name__ == '__main__':
    daily_hot = QQDailyHot()
    daily_hot.create_post_from_daily_hot()
    daily_hot.quit()
