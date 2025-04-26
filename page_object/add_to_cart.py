import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddToCart:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def add_random_item_to_cart(self):
        buttons = self.browser.find_elements(By.CSS_SELECTOR, 'button[title="Add to Cart"]')
        random_button = random.choice(buttons)
        self.browser.execute_script("arguments[0].scrollIntoView();", random_button)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(random_button)).click()

    def opencart_dropdown(self):
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        dropdown_button = self.wait.until \
        (EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-bs-toggle="dropdown"]')))
        dropdown_button.click()

    def remove_product_from_cart(self):
        remove_buttons = self.browser.find_elements(By.CLASS_NAME, "btn.btn-danger")
        if remove_buttons:
            remove_buttons[0].click()
        else:
            raise Exception("Товар не добавлен в корзину")