from locators import PageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def use_search_form(self,id_product):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element(*PageLocators.search_form_path)
        element.send_keys(id_product)

    def click_search_button(self):
        self.driver.implicitly_wait(20)
        element1 = self.driver.find_element(*PageLocators.search_button_path)
        element1.click()

    def go_to_basket(self):
        self.driver.implicitly_wait(20)
        element2 = self.driver.find_element(*PageLocators.basket_path)
        element2.click()

class ProductPage(BasePage):

    def click_buy_button(self):
        self.driver.implicitly_wait(20)
        element3 = self.driver.find_element(*PageLocators.buy_button_path)
        element3.click()

    def click_close_button(self):
        self.driver.implicitly_wait(20)
        element4 = self.driver.find_element(*PageLocators.close_button_path)
        element4.click()

    def return_to_mainpage(self):
        self.driver.implicitly_wait(20)
        element5 = self.driver.find_element(*PageLocators.main_page_path)
        element5.click()

class Basket(BasePage):
    def find_product_title(self):
        self.driver.implicitly_wait(20)
        element6 = self.driver.find_element(*PageLocators.product_title)
        return element6
