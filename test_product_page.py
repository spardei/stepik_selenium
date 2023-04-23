from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.links import product_link, login_link
import time
import pytest
from faker import Faker


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, login_link)
        self.page.open()
        fake = Faker()
        email = fake.email()
        password = "12QW34as56ZX"
        self.page.register_new_user(email=email, password=password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.add_to_cart()
        self.page.solve_quiz_and_get_code()

    def test_user_cant_see_success_message(self, browser):
        self.page = ProductPage(browser, product_link)
        self.page.open()
        self.page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.open_basket()
    page = BasketPage(browser)
    page.empty_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()
