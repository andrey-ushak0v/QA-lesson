import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#def test_ajax_request(driver):
#    driver.get("http://www.uitestingplayground.com/ajax")
#    wait = WebDriverWait(driver, 90)
#    ajax_button = driver.find_element(By.ID, 'ajaxButton')
#    ajax_button.click()
#
#    ajax_text = wait.until(
#        EC.text_to_be_present_in_element(
#            (By.CLASS_NAME, 'bg-success'), "Data loaded with AJAX get request."
#        )
#    )
#    assert ajax_text, 'искомый текст не отобразился'
#
#
#def test_ajax_request_implicit(driver):
#    driver.get("http://www.uitestingplayground.com/ajax")
#    driver.implicitly_wait(20)
#    ajax_button = driver.find_element(By.ID, 'ajaxButton')
#    ajax_button.click()
#
#    ajax_text = driver.find_element(By.CLASS_NAME, 'bg-success')
#
#    assert "Data loaded with AJAX get request." in ajax_text.text, 'искомый текст не загрузился'
#
#
#def test_ajax_request_with_sleep(driver):
#    driver.get("http://www.uitestingplayground.com/ajax")
#    ajax_button = driver.find_element(By.ID, 'ajaxButton')
#    ajax_button.click()
#    time.sleep(20)
#    ajax_text = driver.find_element(By.CLASS_NAME, 'bg-success')
#    assert "Data loaded with AJAX get request." in ajax_text.text, 'искомый текст не загрузился'


#def test_wait_for_button(driver):
#    driver.get("http://www.uitestingplayground.com/loaddelay")
#    wait = WebDriverWait(driver, 10)
#    button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Button Appearing After Delay']")))
#    assert button.is_displayed(), "кнопки нет"
#
#def test_login_to_orangehrm(driver):
#
#    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#    wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд
#    # Вводим имя пользователя
#    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#    username_field.send_keys("Admin")
#
#    # Вводим пароль
#    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
#    password_field.send_keys("admin123")
#
#    # Нажимаем кнопку Login
#    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#    login_button.click()
#
#    # Ожидаем, пока URL изменится и будет содержать "dashboard"
#    wait.until(EC.url_contains("dashboard"))
#
#    # Проверяем, что в URL содержится "dashboard"
#    assert "dashboard" in driver.current_url, f"Ожидаемый URL не содержит 'dashboard': {driver.current_url}"
