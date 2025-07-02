from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):
    TC_LINK = (By.CSS_SELECTOR, "a[href*='/c/terms-conditions']")

    def verify_sign_in_page(self):
        self.verify_partial_url('/login')

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_conditions_link(self):
        self.click(*self.TC_LINK)