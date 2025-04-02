import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ajax_request(driver):
    driver.get("http://www.uitestingplayground.com/ajax")
    wait = WebDriverWait(driver, 90)
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()

    ajax_text = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'bg-success'), "Data loaded with AJAX get request."
        )
    )
    assert ajax_text, 'искомый текст не отобразился'


def test_ajax_request_implicit(driver):
    driver.get("http://www.uitestingplayground.com/ajax")
    driver.implicitly_wait(20)
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()

    ajax_text = driver.find_element(By.CLASS_NAME, 'bg-success')

    assert "Data loaded with AJAX get request." in ajax_text.text, 'искомый текст не загрузился'


def test_ajax_request_with_sleep(driver):
    driver.get("http://www.uitestingplayground.com/ajax")
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()
    time.sleep(20)
    ajax_text = driver.find_element(By.CLASS_NAME, 'bg-success')
    assert "Data loaded with AJAX get request." in ajax_text.text, 'искомый текст не загрузился'

