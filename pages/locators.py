from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN = "login"
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    MESSAGES_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner")
    PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_OF_PRODUCT_ON_MAIN_PAGE = (By.CSS_SELECTOR, "p.price_color")
