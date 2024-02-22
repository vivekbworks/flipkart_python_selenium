from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from testsuite.src.homepageLocators import *


def enter_text_into_search_box_and_verify_result(driver, text_to_search):
    search_box = driver.find_element(By.XPATH, search_box_loc)
    search_box.send_keys(text_to_search)
    search_box.send_keys(Keys.ENTER)
    search_result = driver.find_element(By.XPATH, search_result_loc).text
    print(search_result)
    expected_text = f'results for "{text_to_search}"'
    assert expected_text in search_result, f"search result are not matched with actual result. Actual text: {search_result}"

def click_on_compare_box_of_tenth_and_elevent_phone_and_verify_it_is_successfully_added_in_compare_tray(driver):
    driver.find_element(By.XPATH, tenth_phone_compare_loc).click()
    driver.find_element(By.XPATH, eleventh_phone_compare_loc).click()
    compare_items_number = driver.find_element(By.XPATH, compare_box_digit_loc).text
    assert compare_items_number == '2', f"number of items in compare box is not matches with expected number. Actual number is : {compare_items_number}"

def get_the_name_of_tenth_phone_and_click_on_it(driver):
    tenth_phone_price = driver.find_element(By.XPATH, price_tenth_phone_loc).text
    tenth_phone_name = driver.find_element(By.XPATH, name_tenth_phone_loc)
    tenth_phone_text = tenth_phone_name.text
    tenth_phone_name.click()
    return tenth_phone_price, tenth_phone_text
