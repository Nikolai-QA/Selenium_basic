from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, browser):
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-bs-toggle="collapse"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Products"]'))).click()
