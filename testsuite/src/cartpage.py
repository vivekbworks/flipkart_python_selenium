import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from testsuite.src.cartpageLocators import *


def switch_to_new_window(driver):
    all_windows = driver.window_handles
    new_window = all_windows[1]
    driver.switch_to.window(new_window)

def click_on_add_to_cart_and_verify_total_price_is_same_as_display_price(driver, tenth_phone_price):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, add_to_cart_btn))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, total_amount_loc)))
    total_amount = driver.find_element(By.XPATH, total_amount_loc).text
    assert total_amount == tenth_phone_price, f"total price is not matches with display price on list. Total price is : {total_amount} and display price is : {tenth_phone_price}"

def click_on_plus_sign_and_verify_it_shows_notificatios(driver, tenth_phone_text):
    plus_btn = driver.find_element(By.XPATH, plus_btn_loc)
    driver.execute_script("arguments[0].scrollIntoView();", plus_btn)
    plus_btn.click()
    msg_after_click_plus_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, notification_loc))).text
    print(msg_after_click_plus_btn)
    assert f"You've changed '{tenth_phone_text}' QUANTITY to '2'" in msg_after_click_plus_btn, "can not add one more item to cart"
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, notification_loc)))

def click_on_remove_and_verify_item_removed_from_cart(driver, tenth_phone_text):
    driver.find_element(By.XPATH, remove_btn_loc).click()
    driver.find_element(By.XPATH, remove_btn_popup).click()
    successfully_remove_msg = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, notification_loc))).text
    print(successfully_remove_msg)
    remove_phone_msg = f'{tenth_phone_text} from your cart'
    assert remove_phone_msg in successfully_remove_msg, "seems like item is not removed yet from cart"

def Verify_missing_cart_message_and_login_message_are_visible(driver):
    missing_cart_msg = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, missing_cart_text_loc))).text
    assert 'Missing Cart items?' in missing_cart_msg, "Missing Cart items? text not visible on screen"
    login_to_see_msg = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, login_to_see_loc))).text
    assert 'Login to see' in login_to_see_msg, "Login to see text not visible on screen"