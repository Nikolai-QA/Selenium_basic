from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CurrencySwitch:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def currency_switch(self, currency_symbol):
        # Получаем цену до изменения валюты
        price_element = self.browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/strong')
        previous_price = price_element.text

        # Открываем переключатель валют
        self.browser.find_element(By.CLASS_NAME, "dropdown-toggle").click()

        # Выбираем валюту в зависимости от currency_symbol
        currency_button = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{currency_symbol}']")))
        currency_button.click()

        self.wait.until(EC.staleness_of(price_element))  # Ожидаем, что предыдущий элемент с ценой исчезнет

        # Получаем цену после смены валюты
        updated_price_element = self.browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/strong')
        updated_price = updated_price_element.text

        # Проверяем, что цена изменилась
        assert previous_price != updated_price, f"Цена не обновилась! Предыдущая цена: {previous_price}, новая цена: {updated_price}"