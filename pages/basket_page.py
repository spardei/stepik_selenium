from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def items_in_basket(self):
        element = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS)
        a = element.text.split()
        b = ' '.join(a)
        return b

    def empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket is not empty."

    def product_in_basket(self, product_name):
        assert product_name in self.items_in_basket(), "Product not in basket."

    def product_price_in_basket(self, product_price):
        assert product_price in self.items_in_basket(), "Basket sum not equal product price."

