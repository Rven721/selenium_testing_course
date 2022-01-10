from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*PPL.ADD_TO_BASKET_BUTTON), 'Cant find add_to_basket button'

    def should_be_price(self):
        assert self.is_element_present(*PPL.BOOK_PRICE), "Cant find book price"

    def should_be_book_name(self):
        assert self.is_element_present(*PPL.BOOK_TITLE), "Cant find book name"

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*PPL.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
    
    def book_price_check(self):
        book_price = self.browser.find_element(*PPL.BOOK_PRICE).text
        #message_book_price = self.browser.find_element(*PPL.MESSAGE_BASKET_PRICE).text
        assert WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(PPL.MESSAGE_BASKET_PRICE, book_price)), 'Book prise is incorrect'

    def book_title_check(self):
        book_title = self.browser.find_element(*PPL.BOOK_TITLE).text
        message_book_title = self.browser.find_element(*PPL.MESSAGE_BOOK_TITLE).text
        assert book_title == message_book_title, 'Book title is incorrect'
    
    def no_success_message_check(self):
        assert self.is_not_element_present(*PPL.MESSAGE_BOOK_TITLE), 'User can seee sccess message'


    def success_message_is_disapeared(self):
        assert self.is_disappeared(*PPL.MESSAGE_BOOK_TITLE), 'The success message was not deiapeared'

