__author__ = 'EddyJones'

url = {
    'start_url': 'http://www.bing.com'
}


def is_search_term_in_title(search_term, driver):
    """I would normally put this in a bing_result_page 'class' but it fits here for this example"""
    return search_term + " - Bing" == driver.title


def is_image_results_section_present(driver):
    return len(driver.find_elements_by_class_name("dg_u")) != 0






