from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    def verify_message_empty_cart(self):
        self.find_element(By.XPATH, "//h1[text()='Your cart is empty']").click()