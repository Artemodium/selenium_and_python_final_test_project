from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        link.click()

    def should_be_verified_after_add_to_basket(self):
        self.should_be_message_product_in_basket_valid()
        self.should_be_product_price_valid()

    def should_be_message_product_in_basket_valid(self):
        try:
            assert self.browser.find_elements(*ProductPageLocators.MESSAGES_AFTER_ADD_TO_BASKET)[0].text ==\
                self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text + " был добавлен в вашу корзину.",\
                "Message or name of product is not valid"
        except NoSuchElementException:
            assert False
        assert True

    def should_be_product_price_valid(self):
        try:
            assert self.browser.find_elements(*ProductPageLocators.PRICE_OF_PRODUCT_IN_BASKET)[-1].text == \
                   self.browser.find_element(
                       *ProductPageLocators.PRICE_OF_PRODUCT_ON_MAIN_PAGE).text, "Price is not valid"
        except NoSuchElementException:
            assert False
        assert True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_AFTER_ADD_TO_BASKET), \
                "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES_AFTER_ADD_TO_BASKET), \
                "Success message is not disappeared, but should be"



