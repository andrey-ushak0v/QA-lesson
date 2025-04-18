import pytest
from selenium import webdriver
from tests_lesson_pom.pages.login_page import LoginPage



def setup_driver():
   driver = webdriver.Chrome()
   driver.maximize_window()
   return driver


@pytest.fixture(scope="class")
def driver():
   driver = setup_driver()
   driver.get("https://www.saucedemo.com/")
   yield driver
   driver.quit()

def test_successful_login(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("standard_user")
   login_page.enter_password("secret_sauce")
   login_page.click_on_login_button()
   assert "inventory.html" in driver.current_url, "Не удалось войти в систему."


def test_invalid_password(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("standard_user")
   login_page.enter_password("wrong_password")
   login_page.click_on_login_button()
   error_msg = login_page.get_error_msg()
   assert "Username and password do not match" in error_msg.text, "Неверное сообщение об ошибке."


def test_locked_out_user(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("locked_out_user")
   login_page.enter_password("secret_sauce")
   login_page.click_on_login_button()
   error_msg = login_page.get_error_msg()
   assert "Sorry, this user has been locked out." in error_msg.text, "Неверное сообщение об ошибке."


def test_empty_username(driver):
   login_page = LoginPage(driver)
   login_page.enter_password("secret_sauce")
   login_page.click_on_login_button()
   error_msg = login_page.get_error_msg()
   assert "Username is required" in error_msg.text, "Неверное сообщение об ошибке."


def test_empty_password(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("standard_user")
   login_page.click_on_login_button()
   error_msg = login_page.get_error_msg()
   assert "Password is required" in error_msg.text, "Неверное сообщение об ошибке."

