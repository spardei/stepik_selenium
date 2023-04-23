from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url=None, timeout=10):
        self.browser = browser
        self.url = url if url else self.browser.current_url
        self.timeout = timeout
        self.wait = WebDriverWait(self.browser, self.timeout)

    def wait_for_element_present(self, how, what):
        try:
            self.wait.until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print(f"Element with {how}='{what}' not found on the page within {self.timeout} seconds.")

    def wait_for_element_visible(self, how, what):
        try:
            self.wait.until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            print(f"Element with {how}='{what}' not visible on the page within {self.timeout} seconds.")

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open_basket(self):
        button = self.browser.find_element(*BasePageLocators.OPEN_BASKET)
        button.click()
        ### return page класс новой страницы

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
