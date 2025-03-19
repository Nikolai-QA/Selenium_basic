from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://192.168.100.49:8081"
ADMIN_URL = f"{BASE_URL}/administration"


def test_admin_login_logout(browser):
    browser.get(ADMIN_URL)
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.ID, "input-password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    WebDriverWait(browser, 0.01).until(EC.url_contains("dashboard&user_token"))
    button_logout = WebDriverWait(browser, 0.01).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/ul/li[4]/a/span")))
    # Проверяем, что логин успешен
    assert "dashboard&user_token" in browser.current_url.lower()
    assert button_logout.text == "Logout"
    # Разлогиниваемся
    browser.find_element(By.CLASS_NAME, "nav-link").click()
    assert "administration" in browser.current_url.lower()
