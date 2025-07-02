from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
# sergio

@then("Verify that “Your cart is empty” message is shown.")
def verify_message_empty_cart(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")


# @then("Verify that “Your cart is empty” message is shown.")
# def verify_cart_empty(context):
#     # context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
#     context.app.cart_page.verify_cart_empty()

# @then("Verify cart page opened")
# def cart_opened(context):
#     context.app.cart_page.verify_cart_opened()
#
#
# @then("verify {item} was added to cart")
# def open_cart(context, item):
#     context.app.cart_page.open_cart()
#
#
# @then('Verify cart has {amount} item(s)')
# def verify_cart_items(context, amount):
#     context.app.cart_page.verify_cart_items(amount)