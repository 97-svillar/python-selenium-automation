
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon'")
    ACCT_BTN = (By.CSS_SELECTOR, "span.sc-b1397f11-3.deTpgY.h-margin-r-x3")
    OPTION_SIGN_IN_BTN = (By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]')


    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)


    def click_cart(self):
        # self.click(*self.CART_ICON)
        self.wait_for_element_click(*self.CART_ICON)

    def click_acct(self):
        self.wait_for_element_click(*self.ACCT_BTN)

    def sign_in(self):
        self.wait_for_element_click(*self.OPTION_SIGN_IN_BTN)