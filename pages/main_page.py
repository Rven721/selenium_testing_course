from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

    def shold_be_language_choose_field(self):
        assert self.is_element_present(*MainPageLocators.LANGUAGE_CHOISE_FIELD), "Language change field is not presented" 

    def shold_be_go_button(self):
        assert self.is_element_present(*MainPageLocators.LANGUAGE_CHOISE_SUBMIT_BUTTON), 'Go button is not presented'

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(self.browser, self.browser.current_url) 
