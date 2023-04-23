import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.product_name()
    product_price = page.product_price()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.open_basket()
    page = BasketPage(browser)
    page.product_in_basket(product_name)
    page.product_price_in_basket(product_price)
