from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        time.sleep(5)
        login_link.click()
        time.sleep(4)

    def should_be_login_link(self):
        time.sleep(5)
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        time.sleep(3)