from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, browser):
        self.browser = browser
        self.url = "http://192.168.100.49:8081/administration"
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.browser.get(self.url)

    def login_admin(self):
        self.browser.find_element(By.ID, "input-username").send_keys("user")
        self.browser.find_element(By.ID, "input-password").send_keys("bitnami")
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        self.wait.until(EC.url_contains("dashboard&user_token"))
        button_logout = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/ul/li[4]/a/span")))
        # Проверяем, что логин успешен
        assert "dashboard&user_token" in self.browser.current_url.lower()
        assert button_logout.text == "Logout"