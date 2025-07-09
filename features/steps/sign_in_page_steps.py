from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


# @then("Verify that sign in page opens")
# def verify_sign_in_page_opens(context):
#     context.driver.find_element(By.XPATH, "//p[text()='Enter your email or mobile number to continue']")


@then("Verify that sign in page opens")
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()


@given("Open sign in page")
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when("Store original window")
def store_window(context):
    context.original_window = context.app.sign_in_page.get_current_window_id()


@when("Click on Target terms and conditions link")
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_terms_conditions_link()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_opened()


@then("User can close new window and switch back to original")
def user_close_new_window(context):
    context.app.base_page.close_window()
    context.app.base_page.switch_to_window_by_id(context.original_window)


@when("enter {valid_email} and select continue")
def enter_valid_email(context, valid_email):
    context.app.sign_in_page.enter_valid_email(valid_email)

@when("enter {invalid_password} and selects continue")
def enter_invalid_password(context, invalid_password):
    context.app.sign_in_page.enter_invalid_password(invalid_password)

@then("verify error message is shown")
def verify_error_message(context):
    context.app.sign_in_page.verify_error_message()