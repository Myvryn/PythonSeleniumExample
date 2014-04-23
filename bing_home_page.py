__author__ = 'EddyJones'

url = {
    'start_url': 'http://www.bing.com'
}

menu_bar = {
    'link_images': 'link_text.IMAGES',
    'link_videos': 'id.scpt1',
    'link_maps': 'id.scpt2',
    'link_news': 'id.scpt3',
    'link_search_history': 'id.scpt4',
    'link_more': 'id.scpt5',
    'link_msn': 'id.scpt6',
    'link_outlook_dot_com': 'id.scpt7',
    'link_make_bing_homepage': 'id.id_d'
}

main_page = {
    'textbox_search': 'id.sb_form_q',
    'button_go': 'id.sb_form_go'
}

results_page = {
    'image_results_section': 'id.dg_c'
}


def get_object_type(item):
    """Returns the type of identifier used by the object."""
    return item.split('.')[0]


def get_object_name(item):
    """Returns the name of the identifier used by the object"""
    return item.split('.')[1]


def enter_text_in_search_box(text, driver):
    """Enters the passed text into the Bing Search Box"""
    search_box = get_selenium_element(main_page['textbox_search'], driver)
    search_box.clear()
    search_box.send_keys(text)
    return


def click_the_go_button(driver):
    """Clicks the search submit button"""
    go_button = get_selenium_element(main_page['button_go'], driver)
    go_button.click()
    return


def click_the_images_link(driver):
    images_link = get_selenium_element(menu_bar['link_images'], driver)
    images_link.click()
    return


def is_search_term_in_title(search_term, driver):
    """I would normally put this in a bing_result_page 'class' but it fits here for this example"""
    return search_term + " - Bing" == driver.title


def is_image_results_section_present(driver):
    images_exist = len(driver.find_elements_by_class_name("dg_u")) != 0
    return images_exist


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



