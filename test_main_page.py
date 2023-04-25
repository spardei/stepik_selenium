import pytest
from .pages.main_page import MainPage
from .pages.links import main_link


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        self.page = MainPage(browser, main_link)
        self.page.open()
        self.page = self.page.go_to_login_page()
        self.page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.page = MainPage(browser, main_link)
        self.page.open()
        self.page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page = page.go_to_login_page()
    page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page = page.open_basket()
    page.empty_basket()
