__author__ = 'EddyJones'

from selenium import webdriver


def choose_web_driver(browser):
    if browser.lower() == 'firefox':
        return webdriver.Firefox()
    if browser.lower() == 'ie':
        return webdriver.Ie()
    if browser.lower() == 'chrome':
        return webdriver.Chrome()
    if browser.lower() == 'opera':
        return webdriver.Opera()
    else:
        return webdriver.Firefox()


def get_object_name(item):
    """Returns the name of the identifier used by the object"""
    return item.split('.')[1]


def get_object_type(item):
    """Returns the type of identifier used by the object."""
    return item.split('.')[0]


def get_selenium_element(element, driver):
    """Returns the selenium element by parsing the dictionary's id"""
    item_type = element.split('.')[0]
    item_id = element.split('.')[1]
    if item_type == 'id':
        element = driver.find_element_by_id(item_id)
    elif item_type == 'link_text':
        element = driver.find_element_by_link_text(item_id)
    elif item_type == 'class':
        element = driver.find_element_by_class_name(item_id)
    else:
        element = driver.find_element_by_name(item_id)
    return element