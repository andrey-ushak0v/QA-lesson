import pytest
from selenium import webdriver
from tests_lesson_pom.pages.inventory_page import InventoryPage
from tests_lesson_pom.pages.login_page import LoginPage




class TestInventory:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        LoginPage(driver).success_login()
        yield driver
        driver.quit()


    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)


    #@pytest.fixture(scope="class")
    #def login_page(self, driver):
    #    return LoginPage(driver)


    def test_items_amount(self, inventory_page):
        assert inventory_page.get_items_amount() == 6, "Количество товаров не совпадает."

    def test_all_items_are_displayed(self, inventory_page):
        assert inventory_page.all_items_are_displayed(), "Не все товары отображаются."

    def test_all_items_names_are_displayed(self, inventory_page):
        assert inventory_page.all_items_names_are_displayed(), "Не все названия товаров отображаются."

    def test_all_item_names_are_not_empty(self, inventory_page):
        assert inventory_page.all_item_names_are_not_empty(), "Есть товары с пустыми названиями."

    def test_all_item_names_contains_sauce_labs(self, inventory_page):
        assert inventory_page.all_item_names_contains_sauce_labs(), "Не все товары начинаются с 'Sauce Labs'."

    def test_backpack_cost(self, login_page, inventory_page, cart_page):
        # 1. Login with valid data
        login_page.success_login("standard_user", "secret_sauce")

        # 2. Remember the cost of the item "Backpack"
        backpack_price = inventory_page.get_item_price("Sauce Labs Backpack")

        # 3. Add item "Backpack" to the cart
        inventory_page.add_item_to_cart("Sauce Labs Backpack")

        # 4. Click on the cart button
