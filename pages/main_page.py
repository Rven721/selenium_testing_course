from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#login_link'), 'Login link is not presented'

    def shold_be_language_choose_field(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#language_selector [name='language']"), "Language change field is not presented" 

    def shold_be_go_button(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#language_selector button'), 'Go button is not presented'

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR,'#login_link')
        login_link.click()

