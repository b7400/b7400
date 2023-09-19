from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL = (By.ID, 'ap_email')

    def verify_signin_opens(self):
        self.verify_element_text('Sign in', *self.SIGNIN_HEADER)
        self.find_element(*self.EMAIL)
