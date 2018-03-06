# encoding: utf-8
"""
从weibo.com获取前20条热门话题
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
import unittest
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Weibo():
    def __init__(self):
        self.dr = webdriver.Firefox()

    @property
    def hot_topic_page_1_url(self):
        return 'http://d.weibo.com/100803?cfs=&Pl_Discover_Pt6Rank__5_filter=hothtlist_type%3D1#_0'

    @property
    def hot_topic_page_2_url(self):
        return 'http://d.weibo.com/100803?cfs=920&Pl_Discover_Pt6Rank__5_filter=hothtlist_type&Pl_Discover_Pt6Rank__5_page=2#Pl_Discover_Pt6Rank__5'

    @property
    def hots_url(self):
        return 'http://d.weibo.com/102803?from=unlogin_home&mod=pindao&type=hotweibo'

    def get_top_20_hot_topics(self):
        first_part = self.get_first_15_hots()
        last_part = self.get_last_5_hots()
        for item in last_part:
            first_part.append(item)
        print(first_part)

        return first_part

    def get_top_10_hots(self):
        hots = []
        self.dr.get(self.hots_url)
        time.sleep(3)
        self.wait_js_complete('.WB_cardwrap')

        wrap_div = self.dr.find_element_by_css_selector('.WB_feed')
        cards = wrap_div.find_elements_by_css_selector('.WB_cardwrap')
        for card in cards[:-2]:
            item = {}
            item['author'] = card.find_element_by_class_name('W_f14').text
            item['content'] = card.find_element_by_css_selector('.WB_text').text
            item['forward'] = card.find_element_by_css_selector('span[node-type="forward_btn_text"]').text
            item['comment'] = card.find_element_by_css_selector('span[node-type="comment_btn_text"]').text
            item['up'] = card.find_elements_by_css_selector('.WB_feed_handle li')[-1].text
            hots.append(item)
        return hots

    def wait_js_complete(self, target_elm_css):
        def element_present(dr, css_selector):
            try:
                elm = self.dr.find_element_by_css_selector(css_selector)
                if elm.is_displayed():
                    return True
                else:
                    return False
            except:
                return False

        Wait(self.dr, 5).until(lambda dr: element_present(dr, target_elm_css))

    def get_first_15_hots(self):
        hots = []
        self.dr.get(self.hot_topic_page_1_url)
        time.sleep(3)
        self.wait_js_complete('.DSC_topicon')
        hot_divs = self.dr.find_elements_by_css_selector('#Pl_Discover_Pt6Rank__5 .info_box')
        for div in hot_divs:
            item = {}
            item['order'] = div.find_element_by_css_selector('.W_autocut>:first-child').text
            if 'TOP' in item['order']:
                item['order'] = item['order'].replace('TOP', '')
            item['title'] = div.find_element_by_css_selector('.S_txt1').text
            item['tag'] = div.find_element_by_css_selector('.W_btn_tag').text
            item['subtitle'] = div.find_element_by_css_selector('.subtitle').text
            item['page_view'] = div.find_element_by_class_name('number').text
            hots.append(item)
        return hots

    def get_last_5_hots(self):
        hots = []
        self.dr.get(self.hot_topic_page_2_url)
        time.sleep(3)
        self.wait_js_complete('.DSC_topicon')
        hot_divs = self.dr.find_elements_by_css_selector('#Pl_Discover_Pt6Rank__5 .info_box')
        for div in hot_divs:
            item = {}
            item['order'] = div.find_element_by_css_selector('.W_autocut>:first-child').text
            if item['order'] == '21':
                break
            item['title'] = div.find_element_by_css_selector('.S_txt1').text
            item['tag'] = div.find_element_by_css_selector('.W_btn_tag').text
            item['subtitle'] = div.find_element_by_css_selector('.subtitle').text
            item['page_view'] = div.find_element_by_class_name('number').text
            hots.append(item)
        return hots

    def quit(self):
        self.dr.quit()


if __name__ == '__main__':
    # hots = Weibo().get_top_20_hot_topics()
    hots = Weibo().get_top_10_hots()
    print(hots)
