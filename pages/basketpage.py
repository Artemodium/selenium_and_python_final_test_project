from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket is not empty!"

    def should_be_message_no_product_in_basket(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text == \
               "Your basket is empty. Continue shopping", "Massage in basket is invalid"
