from selenium.webdriver.common.by import By

class PageLocators(object):

    search_form_path = (By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input")
    search_button_path = (By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button")
    buy_button_path = (By.XPATH, "/html/body/app-root/div/div/rz-product/div/product-tab-main/div[1]/div[1]/div[2]/rz-product-main-info/div[2]/div/ul/li[1]/app-product-buy-btn/app-buy-button/button")
    close_button_path = (By.XPATH, "/html/body/app-root/single-modal-window/div[3]/div[1]/button")
    main_page_path = (By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/a/picture/img")
    basket_path = (By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[7]/rz-cart/button")
    product_title = (By.XPATH, "/html/body/app-root/single-modal-window/div[3]/div[2]/rz-shopping-cart/div/ul/li/rz-cart-product/div/div[1]/div/a")
