from frameworks.page.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class PostListPage(BasePage):
    @property
    def first_post(self):
        return self.by_css('.row-title')

    def row(self, post_id):
        row_id = "post-" + post_id
        return self.by_id(row_id)

    def row_find_by_id(self, post_id):
        row_id = "post-" + post_id
        return self.driver.find_element_by_id(row_id)

    def delete_post_by_id(self, post_id):
        post_row = self.row(post_id)
        ActionChains(self.driver).move_to_element(post_row).perform()
        post_row.find_element_by_css_selector('a.submitdelete').click()
