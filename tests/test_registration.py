from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_object.main_page import MainPage


def test_registration(browser):
    page = MainPage(browser)
    wait = WebDriverWait(browser, 10)
    page.open()
    browser.find_element(By.XPATH, '//span[text()="My Account"]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Register"]'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "input-firstname"))).send_keys("test")
    browser.find_element(By.ID, "input-lastname").send_keys("test")
    browser.find_element(By.ID, "input-email").send_keys("test@test.com")
    browser.find_element(By.ID, "input-password").send_keys("test")
    browser.find_element(By.NAME, "agree").click()
    browser.find_element(By.XPATH, '//button[text()="Continue"]').click()
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Your Account Has Been Created!"]')))
    assert success_message.text == "Your Account Has Been Created!"
