# coding=utf-8
# 登录


def login(self, username, password):
    dr = self.dr
    dr.switch_to_frame("x-URS-iframe")
    dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").clear()
    dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys(username)
    dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
    dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").send_keys(password)
    dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a").click()


# 退出
def logout(self):
    dr = self.dr
    dr.find_element_by_link_text(u"退出").click()

