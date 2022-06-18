import unittest
from selenium import webdriver
import page
from webdriver_manager.chrome import ChromeDriverManager

class RozetkaTest(unittest.TestCase):

    id_prod = 'MD506Z/A' #id product for search

    def setUp(self):
        #Driver init
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://rozetka.com.ua/")

    def test_rozetka(self):
        main_page = page.MainPage(self.driver)
        product_page = page.ProductPage(self.driver)
        main_page.use_search_form(self.id_prod) #Find by id_product through search panel
        main_page.click_search_button() #Click on search button
        basket_page = product_page.click_buy_button() #Click on buy button
        basket_page.click_close_button() #Close shopping cart popup
        product_page.return_to_mainpage() #Return to main page
        main_page.go_to_basket() #go to shopping cart
        title = basket_page.find_product_title()
        assert self.id_prod in title #check the product is added

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

