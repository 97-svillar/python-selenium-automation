# Locators for Amazon Sign-In page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
sleep(10)
# Locators:
# Amazon Logo
driver.find_element(By.XPATH, "//i[contains(@class, 'a-icon-logo')]")
print('I found the logo!')

#Email Field
driver.find_element(By.XPATH, "//input[@type='email' and @name='email']" )
print("I found the email field!")

#Conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, '_condition_of_use?')]")
print("I found the condition of use!")
driver.quit()

# Homework part 2
# 3 A's: Arrange / Act / Assert
# Arrange
# init driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# open the url
driver.get('https://www.target.com/')
sleep(7)

# Act
driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']").click()
sleep(7)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(5)

# Assert (Verification)
expected_text = 'Sign in or create account'
actual_text = driver.find_element(By.XPATH, "//h1[@class='styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny']").text

assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'
print('Test case passed')

driver.find_element(By.XPATH, "//button[@class='styles_ndsBaseButton__W8Gl7 styles_lg___H2IL styles_lgGap__bPB7P styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_lg__T5sAi styles_filleddefault__7QnWt']")
print("I found the button!")
driver.quit()