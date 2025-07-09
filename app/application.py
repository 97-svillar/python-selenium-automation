
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.sign_in_page import SignIn
from pages.terms_conditions_page import TermsConditionsPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.help_page = HelpPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.sign_in_page = SignIn(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)