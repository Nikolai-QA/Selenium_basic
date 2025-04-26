from page_object.main_page import MainPage
from page_object.add_to_cart import AddToCart


def test_add_random_item_to_cart(browser):
    page = MainPage(browser)
    cart = AddToCart(browser)
    page.open()
    cart.add_random_item_to_cart()
    cart.opencart_dropdown()
    cart.remove_product_from_cart()
