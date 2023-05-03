import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators


url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()

@pytest.fixture()
def login(driver):
    driver.find_element(*TestLocators.LOGIN_IN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_TEXT_AFTER_REG)))
    driver.find_element(*TestLocators.EMAIL_FIELD_IN_LOGIN_FORM).send_keys('vasilia_buskina_08_123@yandex.ru')
    driver.find_element(*TestLocators.PASSWORD_FIELD_IN_LOGIN_FORM).send_keys('yandex123')
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    return driver
