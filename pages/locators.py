from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LANGUAGE_CHOISE_FIELD = (By.CSS_SELECTOR, "#language_selector [name='language']")
    LANGUAGE_CHOISE_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#language_selector button') 
    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
