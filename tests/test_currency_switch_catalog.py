import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://192.168.100.49:8081"

@pytest.mark.parametrize("currency_symbol", ["€ Euro", "£ Pound Sterling", "$ US Dollar"])
def test_currency_switch_main_page(browser, currency_symbol):
    wait = WebDriverWait(browser, 10)
    browser.get(f'{BASE_URL}/en-gb/catalog/desktops')

    # Получаем цену до и после изменения валюты
    price_element = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/strong')
    previous_price = price_element.text

    # Открываем переключатель валют
    browser.find_element(By.CLASS_NAME, "dropdown-toggle").click()

    # Выбираем валюту в зависимости от currency_symbol
    currency_button = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{currency_symbol}']")))
    currency_button.click()

    wait.until(EC.staleness_of(price_element))  # Ожидаем, что предыдущий элемент с ценой исчезнет

    # Получаем цену после смены валюты
    updated_price_element = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/strong')
    updated_price = updated_price_element.text

    # Проверяем, что цена изменилась
    assert previous_price != updated_price, f"Цена не обновилась! Предыдущая цена: {previous_price}, новая цена: {updated_price}"

