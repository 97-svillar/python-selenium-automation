from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignIn(Page):
    TC_LINK = (By.CSS_SELECTOR, "a[href*='/c/terms-conditions']")
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    CONTINUE_BTN = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "password--ErrorMessage")

    def verify_sign_in_page(self):
        self.verify_partial_url('/login')

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_conditions_link(self):
        self.click(*self.TC_LINK)

    def enter_valid_email(self, valid_email):
        self.input_text(valid_email, *self.EMAIL)
        self.click(*self.CONTINUE_BTN)
        sleep(2)

    def enter_invalid_password(self, invalid_password):
        self.input_text(invalid_password, *self.PASSWORD)
        self.click(*self.CONTINUE_BTN)
        sleep(2)

    def verify_error_message(self):
        self.find_element(*self.ERROR_MESSAGE)