from locators import PageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def use_search_form(self,id_product):
        element = self.driver.find_element(*PageLocators.search_form_path)
        element.send_keys(id_product)

    def click_search_button(self):
        wait = WebDriverWait(self.driver, 10)
        element_wait = wait.until(EC.element_to_be_clickable(PageLocators.search_button_path))
        element_wait.click()
        time.sleep(2)

    def go_to_basket(self):
        wait = WebDriverWait(self.driver, 10)
        element_wait = wait.until(EC.element_to_be_clickable(PageLocators.basket_path))
        element_wait.click()
        return Basket(self.driver)

class ProductPage(BasePage):

    def click_buy_button(self):
        wait = WebDriverWait(self.driver, 20)
        element_wait = wait.until(EC.element_to_be_clickable(PageLocators.buy_button_path))
        element_wait.click()
        return Basket(self.driver)

    def return_to_mainpage(self):
        wait = WebDriverWait(self.driver, 10)
        element_wait = wait.until(EC.element_to_be_clickable(PageLocators.main_page_path))
        element_wait.click()
        return MainPage(self.driver)

class Basket(BasePage):
    def find_product_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(PageLocators.product_title))
        return element.text

    def click_close_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element_wait = wait.until(EC.element_to_be_clickable(PageLocators.close_button_path))
            element_wait.click()
        except:
            pass

