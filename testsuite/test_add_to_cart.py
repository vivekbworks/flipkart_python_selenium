from testsuite.src.cartpage import *
from testsuite.src.homepage import *
from testsuite.src.login_page import open_browser

# variables
url = "https://www.flipkart.com/"
text_to_search = "mobile"

def add_remove_items_from_cart():
    try:
        driver = open_browser('chrome')
        driver.get(url)
        driver.maximize_window()

        enter_text_into_search_box_and_verify_result(driver, text_to_search)

        click_on_compare_box_of_tenth_and_elevent_phone_and_verify_it_is_successfully_added_in_compare_tray(driver)

        tenth_phone_price, tenth_phone_text = get_the_name_of_tenth_phone_and_click_on_it(driver)

        switch_to_new_window(driver)

        click_on_add_to_cart_and_verify_total_price_is_same_as_display_price(driver, tenth_phone_price)

        click_on_plus_sign_and_verify_it_shows_notificatios(driver)

        click_on_remove_and_verify_item_removed_from_cart(driver, tenth_phone_text)

        Verify_missing_cart_message_and_login_message_are_visible(driver)

    except Exception as e:
        print(f"An error occurred: {e}")

add_remove_items_from_cart()