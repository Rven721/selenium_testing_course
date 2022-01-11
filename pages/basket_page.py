from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FIRST_BASKET_ITEM), 'Found at least one product in the pasket'

    def should_be_empty_basket_message(self):
        control_word = 'empty'
        page_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert control_word in page_message, 'Wrong message on the page. Should be empty message.'
        
