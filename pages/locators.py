from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN = "login"


class ProductPageLocators:
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    MESSAGES_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner")
    PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_OF_PRODUCT_ON_MAIN_PAGE = (By.CSS_SELECTOR, "p.price_color")
