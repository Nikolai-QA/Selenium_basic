import pytest

from page_object.currency_switch import CurrencySwitch
from page_object.main_page import MainPage

@pytest.mark.parametrize("currency_symbol", ["€ Euro", "£ Pound Sterling", "$ US Dollar"])
def test_currency_switch_main_page(browser, currency_symbol):
    page = MainPage(browser)
    currency = CurrencySwitch(browser)
    page.open()
    currency.currency_switch(currency_symbol)
