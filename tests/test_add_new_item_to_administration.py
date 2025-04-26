import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.find_item_in_filter import FindItem
from page_object.login_admin import Login
from page_object.product_page import ProductPage


def test_add_new_item_to_administration(browser):
    login = Login(browser)
    product_page = ProductPage(browser)
    find = FindItem(browser)
    wait = WebDriverWait(browser, 10)
    login.open()
    login.login_admin()
    product_page.open()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Add New"]'))).click()

    wait.until(EC.element_to_be_clickable((By.ID, 'input-name-1'))).send_keys("Super Computer")
    browser.find_element(By.ID, 'input-meta-title-1').send_keys("super_computer")
    browser.find_element(By.XPATH, '//a[text()="Data"]').click()

    wait.until(EC.element_to_be_clickable((By.ID, 'input-model'))).send_keys("Apple")
    browser.find_element(By.XPATH, '//a[text()="SEO"]').click()

    wait.until(EC.element_to_be_clickable((By.ID, 'input-keyword-0-1'))).send_keys("Keyword")
    browser.find_element(By.CSS_SELECTOR, 'button[title="Save"]').click()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Products"]'))).click()

    # Проверяем что в элементе есть нужный текст
    find.find_item()
    right_product = wait.until(EC.presence_of_element_located((By.XPATH, '//td[contains(text(), "Super Computer")]')))
    time.sleep(2)
    assert "Super Computer" in right_product.text, 'Товар не добавлен в админку!'





