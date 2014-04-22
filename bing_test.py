__author__ = 'EddyJones'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bing_home_page

driver = webdriver.Firefox()

""" TEST:  Navigate to bing.com """
url = bing_home_page.url['start_url']
driver.get(url)
assert "Bing" in driver.title

""" TEST:  Type in a search term and verify that term is in the title bar """
search_terms = ['selenium',
                'esp guitars',
                'classic rock',
                'Mötley Crüe',
                'python using selenium',
                'cake software']
for search_term in search_terms:
    bing_home_page.enter_text_in_search_box(search_term, driver)
    bing_home_page.click_the_go_button(driver)
    assert bing_home_page.is_search_term_in_title(search_term, driver)

driver.close()


