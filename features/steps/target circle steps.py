from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@given("open target circle page")
def open_main(context):
    context.driver.get("https://www.target.com/circle")


@then("verify there at least {number} benefit cells")
def verify_benefit_cells(context, number):
    print(type(number))
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*="sc-acea07d2-5"]')
    print(benefit_cells)

    # benefit cells >= 10
    assert len(benefit_cells) >= int(number), f'Expected {number} benefit cells but got {len(benefit_cells)}'