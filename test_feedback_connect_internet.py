import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
@pytest.mark.parametrize("url", [
    "https://piter-online.net/"
])
def test_feedback(browser,url):
    try:
        link = url
        browser.get(link)
        street_input = browser.find_element(By.XPATH, "//input[@type='text' and @datatest='main_input_street_home_new']")
        street_input.send_keys("Тестовая линия")
        time.sleep(1)
        street_input.send_keys(Keys.ENTER)
        house_number = browser.find_element(By.XPATH, "//span[@id='label' and text()='Дом']/following-sibling::input[@datatest='main_input_street_home_new']")
        time.sleep(1)
        house_number.send_keys("1")
        time.sleep(1)
        search_button = browser.find_element(By.CSS_SELECTOR, "div[data-test='find_tohome_button']").click()
        info_popup = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[datatest="close_popup1_from_quiz_input_tel"]'))
        )
        info_popup.click()
        for i in range(5):
            # Клик по кнопке "Подключить по акции"
            connect_button = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[datatest="providers_form_inspect_connect_tariff_button"]'))
            )
            connect_button.click()

            # Ввод номера телефона в модалке
            phone_input = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[datatest="popup_tariff_order_input_tel"]'))
            )
            phone_input.send_keys("1111111111")
            time.sleep(1)

            # Клик по кнопке "Оставить заявку"
            submit_button = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'div[data-test="popup_tariff_order_form_input_connect_button"]'))
            )
            submit_button.click()
            time.sleep(1)

            # Клик по кнопке закрытия модалки
            close_modal_button = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-test="give_feedback"]'))
            )
            close_modal_button.click()

    finally:
        browser.quit()
