from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


# quick edit
ADD_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor']")
SIDE_NAV_ADD_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButtonOrTextIdFor']")
SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@then('Verify search worked for {product}')
def verify_search_results(context, product):
    # actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    # assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"
    context.app.search_results_page.verify_search_results(product)


@then('add {product} to the cart')
def add_to_cart(context, product):
    context.app.search_results_page.add_product_to_cart()


@then('add {product} to cart on options menu')
def add_to_cart(context, product):
    context.app.search_results_page.add_to_cart_options_menu()