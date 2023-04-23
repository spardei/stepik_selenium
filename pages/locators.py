from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > button")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form > button")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")


class BasketPageLocators:
    PRICE_IN_BASKET = (By.CLASS_NAME, "price_color align-right")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMPTY_BASKET = (By.CLASS_NAME, "content_inner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.PARTIAL_LINK_TEXT, "basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
