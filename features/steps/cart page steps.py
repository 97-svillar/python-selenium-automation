from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
# sergio

@then("Verify that “Your cart is empty” message is shown.")
def verify_message_empty_cart(context):
    # context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
    context.app.cart_page.verify_message_empty_cart()

@then("verify {item} was added to cart")
def open_cart(context, item):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"