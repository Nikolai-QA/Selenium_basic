from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindItem:
    def __init__(self, browser):
        self.wait = WebDriverWait(browser, 10)
        self.browser = browser


    def find_item(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'input-name'))).send_keys("Super Computer")
        self.browser.find_element(By.ID, 'button-filter').click()
