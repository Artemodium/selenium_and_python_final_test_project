from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        time.sleep(5)
        login_link.click()
        time.sleep(4)

    def should_be_login_link(self):
        time.sleep(5)
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        time.sleep(3)