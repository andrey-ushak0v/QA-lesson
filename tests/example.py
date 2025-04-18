#import pytest
#import time
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#
#def test_ajax_request(driver):
#    """тест с явным ожидаением"""
#    driver.get("http://www.uitestingplayground.com/ajax")
#    wait = WebDriverWait(driver, 15)  # Ожидание до 15 секунд
#
#    # Нажимаем на кнопку, которая запускает AJAX-запрос
#    ajax_button = driver.find_element(By.ID, "ajaxButton")
#    ajax_button.click()
#
#    # Ожидаем, пока появится элемент с классом "bg-success" и нужным текстом
#    ajax_text = wait.until(
#        EC.text_to_be_present_in_element(
#            (By.CLASS_NAME, "bg-success"), "Data loaded with AJAX get request."
#        )
#    )
#    # Проверяем, что текст появился
#    assert ajax_text, "Текст 'Data loaded with AJAX get request.' не появился!"
#def test_ajax_request_implicit(driver):
#    driver.implicitly_wait(20)
#    driver.get("http://www.uitestingplayground.com/ajax")
#    # Нажимаем на кнопку AJAX-запроса
#    ajax_button = driver.find_element(By.ID, "ajaxButton")
#    ajax_button.click()
#
#    # Ищем появившийся элемент (Selenium будет ждать до 15 секунд)
#    ajax_text_element = driver.find_element(By.CLASS_NAME, "bg-success")
#
#    # Проверяем, что текст внутри элемента соответствует ожидаемому
#    assert "Data loaded with AJAX get request." in ajax_text_element.text, "Текст не загрузился!"
#
#
#def test_ajax_request_sleep(driver):
#    # Нажимаем на кнопку AJAX-запроса
#    driver.get("http://www.uitestingplayground.com/ajax")
#    ajax_button = driver.find_element(By.ID, "ajaxButton")
#    ajax_button.click()
#
#    # Жёсткое ожидание 15 секунд (плохая практика)
#    time.sleep(20)
#
#    # Находим элемент после ожидания
#    ajax_text_element = driver.find_element(By.CLASS_NAME, "bg-success")
#
#    # Проверяем, что текст внутри элемента соответствует ожидаемому
#    assert "Data loaded with AJAX get request." in ajax_text_element.text, "Текст не загрузился!"
#def test_wait_for_button(driver):
#    driver.get("http://www.uitestingplayground.com/loaddelay")
#    wait = WebDriverWait(driver, 15)  # Ожидание до 15 секунд
#
#    # Ждём, пока кнопка появится на странице
#    button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Button Appearing After Delay']")))
#
#    # Проверяем, что кнопка действительно появилась
#    assert button.is_displayed(), "Кнопка не появилась!"
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
#
#def test_slow_calculator(driver):
#    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#
#    wait = WebDriverWait(driver, 50)  # Ожидание результата
#
#    # Вводим задержку 45 секунд в поле #delay
#    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
#    delay_input.clear()
#    delay_input.send_keys("10")
#
#    # Нажимаем кнопки: 7, +, 8, =
#    driver.find_element(By.XPATH, "//span[text()='7']").click()
#    driver.find_element(By.XPATH, "//span[text()='+']").click()
#    driver.find_element(By.XPATH, "//span[text()='8']").click()
#    time.sleep(3)
#    driver.find_element(By.XPATH, "//span[text()='=']").click()
#
#    # Ждём появления результата "15" через 45 секунд
#    result_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
#    assert result_element, "Ожидаемый результат '15' не отобразился!"





