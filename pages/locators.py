from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LANGUAGE_CHOISE_FIELD = (By.CSS_SELECTOR, "#language_selector [name='language']")
    LANGUAGE_CHOISE_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#language_selector button') 

class MainPageLocators(BasePageLocators):
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_page .product_main .price_color')
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_page h1")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages p strong")
    MESSAGE_BOOK_TITLE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    
