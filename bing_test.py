__author__ = 'EddyJones'

import utilities
import unittest
import bing_page
import common_elements
import time

url = bing_page.url['start_url']


class BingTest(unittest.TestCase):

    def setUp(self):
        self.driver = utilities.choose_web_driver('firefox')
        self.addCleanup(self.driver.quit)

    def test_navigate_to_bing(self):
        self.driver.get(url)
        assert "Bing" in self.driver.title

    def test_search_request_should_be_in_title(self):
        self.driver.get(url)
        self.driver.maximize_window()
        search_terms = ['selenium',
                        'esp guitars',
                        'classic rock',
                        'Mötley Crüe',
                        'python using selenium',
                        'cake software']
        for search_term in search_terms:
            common_elements.enter_text_in_search_box(search_term, self.driver)
            time.sleep(.5)
            common_elements.click_the_go_button(self.driver)
            time.sleep(2)
            assert bing_page.is_search_term_in_title(search_term, self.driver)

    def test_search_for_images(self):
        self.driver.get(url)
        common_elements.click_the_images_link(self.driver)
        search_terms = ['star wars',
                        'star trek',
                        'game of thrones']
        for search_term in search_terms:
            common_elements.enter_text_in_search_box(search_term, self.driver)
            time.sleep(.5)
            common_elements.click_the_go_button(self.driver)
            time.sleep(2)
            assert bing_page.is_image_results_section_present(self.driver)

    def test_search_for_no_images(self):
        self.driver.get(url)
        common_elements.click_the_images_link(self.driver)
        search_terms = ['@$!%$!@']
        for search_term in search_terms:
            common_elements.enter_text_in_search_box(search_term, self.driver)
            common_elements.click_the_go_button(self.driver)
            self.assertFalse(bing_page.is_image_results_section_present(self.driver))



