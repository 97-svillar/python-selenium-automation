from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# sergio

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon'")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
ACCT_BTN = (By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']")


@when('Search for {search_word}')
def search_product(context, search_word):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()
    context.app.header.search_product(search_word)



@when("click on cart")
def click_cart(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart()

@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'


@when('selecting account and clicking sign in')
def click_acct(context):
    context.app.header.click_acct()
    context.app.header.sign_in()