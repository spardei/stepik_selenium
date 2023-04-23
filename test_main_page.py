import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.links import main_link


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        self.page = MainPage(browser, main_link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser)
        self.login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.page = MainPage(browser, main_link)
        self.page.open()
        self.page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.open_basket()
    page = BasketPage(browser)
    page.empty_basket()
