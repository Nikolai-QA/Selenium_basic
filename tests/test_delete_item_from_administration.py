import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_object.find_item_in_filter import FindItem
from page_object.login_admin import Login
from page_object.product_page import ProductPage


def test_delete_item_from_administration(browser):
    login = Login(browser)
    product_page = ProductPage(browser)
    find = FindItem(browser)
    wait = WebDriverWait(browser, 10)
    login.open()
    login.login_admin()
    product_page.open()

    # Опускаемся до стрелочки и нажимаем на нее
    pagination_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.page-link')))
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", pagination_btn)
    time.sleep(1)
    wait.until(EC.element_to_be_clickable(pagination_btn)).click()
    # Находим строку с товаром, который хотим удалить и кликаем на чекбокс
    row = wait.until(EC.presence_of_element_located((By.XPATH, '//tr[td[contains(., "Super Computer")]]')))
    checkbox = row.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    checkbox.click()
    # Поднимаемся к кнопке "Удалить" и удаляем товар
    delete_btn = browser.find_element(By.XPATH, '//button[@title="Delete"]')
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_btn)
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(delete_btn)).click()
    time.sleep(2)
    # После клика по кнопке "Удалить", появляется alert
    alert = wait.until(EC.alert_is_present())
    # Принять alert
    alert.accept()
    # Ждем, пока пропадет строка с товаром
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[td[contains(., "Super Computer")]]')))
    # Проверяем что элемент удален
    find.find_item()
    time.sleep(2)
    # Проверяем, что текст "No results!" появился
    assert wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, '//td[contains(text(), "No results!")]'),
        "No results!")), "Товар Super Computer не удален!"