import pytest
from page_object.catalog_page import CatalogPage
from page_object.currency_switch import CurrencySwitch

@pytest.mark.parametrize("currency_symbol", ["€ Euro", "£ Pound Sterling", "$ US Dollar"])
def test_currency_switch_catalog(browser, currency_symbol):
    page = CatalogPage(browser)
    currency = CurrencySwitch(browser)
    page.open()
    currency.currency_switch(currency_symbol)
