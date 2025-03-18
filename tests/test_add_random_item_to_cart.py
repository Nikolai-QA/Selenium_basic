import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://192.168.100.49:8081"


def test_add_random_product_in_cart(browser):
    wait = WebDriverWait(browser, 10)
    browser.get(BASE_URL)
    buttons = browser.find_elements(By.CSS_SELECTOR, 'button[title="Add to Cart"]')
    random_button = random.choice(buttons)
    browser.execute_script("arguments[0].scrollIntoView();", random_button)
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(random_button)).click()

    browser.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    dropdown_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-bs-toggle="dropdown"]')))
    dropdown_button.click()

    remove_buttons = browser.find_elements(By.CLASS_NAME, "btn.btn-danger")
    if remove_buttons:
        remove_buttons[0].click()
    else:
        raise Exception("Товар не добавлен в корзину")









