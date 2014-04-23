__author__ = 'EddyJones'

import utilities
import unittest
import bing_home_page

url = bing_home_page.url['start_url']


class BingTest(unittest.TestCase):

    def setUp(self):
        self.driver = utilities.choose_web_driver('firefox')
        self.addCleanup(self.driver.quit)

    def test_navigate_to_bing(self):
        self.driver.get(url)
        assert "Bing" in self.driver.title

    def test_search_request_should_be_in_title(self):
        self.driver.get(url)
        search_terms = ['selenium',
                        'esp guitars',
                        'classic rock',
                        'Mötley Crüe',
                        'python using selenium',
                        'cake software']
        for search_term in search_terms:
            bing_home_page.enter_text_in_search_box(search_term, self.driver)
            bing_home_page.click_the_go_button(self.driver)
            assert bing_home_page.is_search_term_in_title(search_term, self.driver)

    def test_search_for_images(self):
        self.driver.get(url)
        bing_home_page.click_the_images_link(self.driver)
        search_terms = ['star wars',
                        'star trek',
                        'game of thrones']
        for search_term in search_terms:
            bing_home_page.enter_text_in_search_box(search_term, self.driver)
            bing_home_page.click_the_go_button(self.driver)
            assert bing_home_page.is_image_results_section_present(self.driver)

    def test_search_for_no_images(self):
        self.driver.get(url)
        bing_home_page.click_the_images_link(self.driver)
        search_terms = ['@$!%$!@']
        for search_term in search_terms:
            bing_home_page.enter_text_in_search_box(search_term, self.driver)
            bing_home_page.click_the_go_button(self.driver)
            self.assertFalse(bing_home_page.is_image_results_section_present(self.driver))



