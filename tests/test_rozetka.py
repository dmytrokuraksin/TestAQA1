import unittest
from selenium import webdriver
import page
from webdriver_manager.chrome import ChromeDriverManager

class Rozetka_test(unittest.TestCase):

    id_prod = 'MD506Z/A'
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://rozetka.com.ua/")

    def test_rozetka(self):
        main_page = page.MainPage(self.driver)
        product_page = page.ProductPage(self.driver)
        main_page.use_search_form(self.id_prod)
        main_page.click_search_button()
        product_page.return_to_mainpage()
        """product_page.click_buy_button()"""
        """basket_page = page.Basket(self.driver)
        title = basket_page.find_product_title()
        assert self.id_prod in title.text"""

    def tearDown(self):
        self.driver.close()

