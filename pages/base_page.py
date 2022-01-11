import math
import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators as BPL
#from .login_page import LoginPage

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
            
    def go_to_login_page(self):
        link = self.browser.find_element(*BPL.LOGIN_LINK)
        link.click()
        #return LoginPage(self.browser, self.browser.current_url)

    def should_be_login_link(self):
        assert self.browser.find_element(*BPL.LOGIN_LINK), 'Login link is not presented'

    def should_be_language_choose_field(self):
        assert self.browser.find_element(*BPL.LANGUAGE_CHOISE_FIELD),'Cant find field to choose language'

    def should_be_go_button(self):
        assert self.browser.find_element(*BPL.LANGUAGE_CHOISE_SUBMIT_BUTTON), 'Cant find a button to submit language change'

    def should_be_basket_button(self):
        assert self.browser.find_element(*BPL.BASKET_BUTTON), 'Cant find a basket button'
     
    def go_to_basket(self):
        basket_button = self.browser.find_element(*BPL.BASKET_BUTTON)        
        basket_button.click()   

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        #time.sleep(5)
        try:
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"The code is {alert_text}")
            alert.accept()
            #time.sleep(10)
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True



