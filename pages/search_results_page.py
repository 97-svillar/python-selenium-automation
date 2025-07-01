
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor']")
    SIDE_NAV_ADD_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButtonOrTextIdFor']")


    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_TXT)

    def add_product_to_cart(self):
        sleep(3)
        self.wait_for_element_click(*self.ADD_CART_BTN)

    def add_to_cart_options_menu(self):
        self.wait_for_element_click(*self.SIDE_NAV_ADD_CART_BTN)