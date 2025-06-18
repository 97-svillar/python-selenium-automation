from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Homework Part 1
# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
sleep(5)

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, "i[class*='a-icon-logo']")
print('I found the logo!')
sleep(5)

# Email Input Field
driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='email']")
print("I found the email field!")
sleep(5)

# Conditions Of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='_condition_of_use?']")
print("I found the condition of use!")
sleep(5)

# --------------------------------------------------------------------------------------------------------

# Homework Part 2

@given("open target main page")
def open_main(context):
    context.driver.get('https://www.target.com/')


@when("click on cart")
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/CartIcon'" ).click()

@then("Verify that “Your cart is empty” message is shown.")
def verify_message_empty_cart(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")

# Test Case 2 Steps

@when("selecting account and clicking sign in")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']").click()
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

@then("Verify that sign in page opens")
def verify_sign_in_page_opens(context):
    context.driver.find_element(By.XPATH, "//p[text()='Enter your email or mobile number to continue']")
