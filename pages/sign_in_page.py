from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):


    def verify_sign_in_page(self):
        self.verify_partial_url('/login')
