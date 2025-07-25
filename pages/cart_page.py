from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    # Copy
    cart_empty_txt = 'Your cart is empty'
    # Locators
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_empty(self):
        self.verify_text(self.cart_empty_txt, *self.CART_EMPTY_MSG)


    def verify_cart_opened(self):
        # self.verify_url('https://www.target.com/cart')
        # self.verify_partial_url('/cart')
        self.wait_for_url_contains('/cart')

    def open_cart(self):
        self.driver.get('https://www.target.com/cart')

    def verify_cart_items(self, amount):
        cart_summary = self.find_element(
            By.XPATH, "//div[./span[contains(text(), 'subtotal')]]"
        ).text
        assert f"{amount} item" in cart_summary, f"Expected {amount} items but got '{cart_summary}'"