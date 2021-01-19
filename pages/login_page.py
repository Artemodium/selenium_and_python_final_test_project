from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        try:
            assert LoginPageLocators.LOGIN_FORM in self.current_url(), "'login' is not present in URL"
        except NoSuchElementException:
            assert False
        assert True

    def should_be_login_form(self):
        try:
            assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login_form is not presented"
        except NoSuchElementException:
            assert False
        assert True

    def should_be_register_form(self):
        try:
            assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register_form is not presented"
        except NoSuchElementException:
            assert False
        assert True
