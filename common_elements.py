from utilities import get_selenium_element

__author__ = 'EddyJones'


menu_bar = {
    'link_images': 'link_text.IMAGES',
    'link_videos': 'link_text.VIDEOS',
    'link_maps': 'link_text_MAPS',
    'link_news': 'link_text.NEWS',
    'link_search_history': 'link_text.SEARCH HISTORY',
    'link_more': 'link_text.MORE',
    'link_msn': 'link_text.MSN',
    'link_outlook_dot_com': 'link_text.OUTLOOK.COM',
    'link_make_bing_homepage': 'link_text.Make Bing my homepage'
}


search_tools = {
    'textbox_search': 'id.sb_form_q',
    'button_go': 'id.sb_form_go'
}


def click_the_images_link(driver):
    images_link = get_selenium_element(menu_bar['link_images'], driver)
    images_link.click()
    return


def enter_text_in_search_box(text, driver):
    """Enters the passed text into the Bing Search Box"""
    search_box = get_selenium_element(search_tools['textbox_search'], driver)
    search_box.clear()
    search_box.send_keys(text)
    return


def click_the_go_button(driver):
    """Clicks the search submit button"""
    go_button = get_selenium_element(search_tools['button_go'], driver)
    go_button.click()
    return