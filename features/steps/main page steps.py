from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# sergio

@given("open target main page")
def open_main(context):
    context.driver.get('https://www.target.com/')