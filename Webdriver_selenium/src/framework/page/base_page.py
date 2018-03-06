from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Webdriver_selenium.src.framework.config.data import CONFIG, ENV
import time
import os

# https://github.com/easonhan007/webdriver_guide/blob/master/34/expected_conditions.py.md

DEFAULT_SECONDS = 5


class BasePage(object):
    url = None
    driver = None
    domain = None

    def __init__(self, driver, path=None):
        self.driver = driver
        self.domain = CONFIG[ENV]['domain']

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

    def navigate(self):
        self.driver.get(self.url)

    def by_id(self, the_id):
        locator = (By.ID, the_id)
        # WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        self.screenshot_on_exception(locator)
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        locator = (By.NAME, the_name)
        # WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        self.screenshot_on_exception(locator)
        return self.driver.find_element_by_name(the_name)

    def by_css(self, css):
        locator = (By.CSS_SELECTOR, css)
        # WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        self.screenshot_on_exception(locator)
        return self.driver.find_element_by_css_selector(css)

    def screenshot_on_exception(self, locator):
        try:
            WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            # print(self.gen_screenshot_path(locator))
            self.driver.get_screenshot_as_file(self.gen_screenshot_path(locator))
            msg = "Time out when locate element using %s: %s" % (locator[0], locator[-1])
            raise TimeoutException(msg)

    def gen_screenshot_path(self, locator):
        locator_str = "NoSuchElement_BY_%s_%s" % (locator[0], locator[-1])
        return "./screenshots/%s_%s.png" % (locator_str, time.time())

    def js(self, js_text):
        return self.driver.execute_script(js_text)
