from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LANGUAGE_CHOISE_FIELD = (By.CSS_SELECTOR, "#language_selector [name='language']")
    LANGUAGE_CHOISE_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#language_selector button') 
    BASKET_BUTTON = (By.CSS_SELECTOR, '.page_inner a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    FIRST_BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items #id_form-0-idll')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p:nth-child(1)")


class MainPageLocators(BasePageLocators):
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_page .product_main .price_color')
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_page h1")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages p strong")
    MESSAGE_BOOK_TITLE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    
