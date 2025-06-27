from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from pages.main_page import MainPage


# sergio

@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main_page()
