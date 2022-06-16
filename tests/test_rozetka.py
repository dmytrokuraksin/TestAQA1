import unittest
from selenium import webdriver
import page
from webdriver_manager.chrome import ChromeDriverManager
import time

class RozetkaTest(unittest.TestCase):

    id_prod = 'MD506Z/A'
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.get("https://rozetka.com.ua/")

    def test_rozetka(self):
        main_page = page.MainPage(self.driver)
        product_page = page.ProductPage(self.driver)
        main_page.use_search_form(self.id_prod)
        main_page.click_search_button()
        time.sleep(5)
        basket_page = product_page.click_buy_button()
        basket_page.click_close_button()
        product_page.return_to_mainpage()
        main_page.go_to_basket()

        title = basket_page.find_product_title()
        assert self.id_prod in title.text

    def tearDown(self):
        self.driver.close()

