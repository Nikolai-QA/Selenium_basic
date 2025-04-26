from selenium.webdriver.common.by import By


class Logout:
    def __init__(self, browser):
        self.browser = browser

    def logout(self):
        self.browser.find_element(By.CLASS_NAME, "nav-link").click()
        assert "administration" in self.browser.current_url.lower()