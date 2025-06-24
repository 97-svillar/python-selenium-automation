from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify search worked for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"


@then('add {product} to the cart')
def add_to_cart(context, product):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor']").click()


@then('add {product} to cart on options menu')
def add_to_cart(context, product):
    sleep(8)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButtonOrTextIdFor']").click()