from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Part 1

# open the url
driver.get(
    "https://www.amazon.com/ap/signin?"
    "openid.pape.max_auth_age=0&"
    "openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2Fref%3Dnav_signin&"
    "openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&"
    "openid.assoc_handle=usflex&"
    "openid.mode=checkid_setup&"
    "openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&"
    "openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
)

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, "i[class*='a-icon-logo']")
print('I found the logo!')
sleep(2)

# Email Input Field
driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='email']")
print("I found the email field!")
sleep(2)

# Conditions Of UseAdd commentMore actions
driver.find_element(By.CSS_SELECTOR, "a[href*='_condition_of_use?']")
print("I found the condition of use!")
sleep(2)