import unittest
from selenium import webdriver
import page
from webdriver_manager.chrome import ChromeDriverManager

class RozetkaTest(unittest.TestCase):

    id_prod = 'MD506Z/A'
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get("https://rozetka.com.ua/")

    def test_rozetka(self):
        main_page = page.MainPage(self.driver)
        product_page = page.ProductPage(self.driver)
        main_page.use_search_form(self.id_prod) #Ввод кода товара в поисковую строку
        main_page.click_search_button() #Нажатие кнопки поиска
        basket_page = product_page.click_buy_button() #Нажатие кнопки купить
        basket_page.click_close_button() #Нажатие кнопки закрыть окно корзины
        product_page.return_to_mainpage() #Возврат на главную страницу
        main_page.go_to_basket() #Переход на страницу корзины
        title = basket_page.find_product_title()
        assert self.id_prod in title #Проверка добавления товара в корзину

    def tearDown(self):
        self.driver.close()

