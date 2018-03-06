# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from framework.config.data import CONFIG
from selenium.common.exceptions import TimeoutException
import time

DEFAULT_SECONDS = 5


class BasePage(object):
    url = None
    driver = None
    domain = None

    def __init__(self, driver, path=None):
        self.driver = driver
        self.domain = CONFIG['domain']

        if path:
            self.url = self.domain + path
        else:
            self.url = None

        if self.url != None:
            self.navigate()

    def title(self):
        return self.driver.get_title()

    def url(self):
        return self.url

    # def fill_form_by_css(self, form_css, value):
    #     elem = self.driver.find_element_by_css_selector(form_css)
    #     elem.send_keys(value)
    #
    # def fill_form_by_id(self, form_element_id, value):
    #     return self.fill_form_by_css('#%s' % form_element_id, value)

    def navigate(self):
        self.driver.get(self.url)

    def by_id(self, the_id):
        locator = (By.ID, the_id)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        locator = (By.NAME, the_name)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_name(the_name)

    def by_css(self, css):
        locator = (By.CSS_SELECTOR, css)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_css_selector(css)

    def by_text_name(self, the_text):
        locator = (By.LINK_TEXT, the_text)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_partial_link_text(the_text)

    def js(self, js_text):
        return self.driver.execute_script(js_text)

    def screenshot_on_exception(self, locator):
        try:
            WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            print(self.gen_screenshot_path(locator))
            self.driver.get_screenshot_as.file(self.gen_screenshot_path(locator))
            # 古霖shit特
            msg = "Time out when locate element using %s: %s" % (locator[0], locator[-1])
            raise TimeoutException(msg)

    def gen_screenshot_path(self, locator):
        locator_str = "NoSuchElement_By_%s_%s" % (locator[0], locator[-1])
        return "./screenshots/%s_%s.png" % (locator_str, time.time())