from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators

def login_fields_form(driver):
    driver.find_element(*TestLocators.EMAIL_FIELD_IN_LOGIN_FORM).send_keys('vasilia_buskina_08_123@yandex.ru')
    driver.find_element(*TestLocators.PASSWORD_FIELD_IN_LOGIN_FORM).send_keys('yandex123')
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()

class TestLogin:

    def test_login_via_login_in_account_button(self, driver):
        driver.find_element(*TestLocators.LOGIN_IN_ACCOUNT_BUTTON).click()
        login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        name = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_PROFILE)).get_attribute("value")
        assert name == "Vasilia"

    def test_login_via_profile_button(self, driver):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        name = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_PROFILE)).get_attribute("value")
        assert name == "Vasilia"

    def test_login_via_button_on_registration_form(self, driver):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_LINK_ON_REG_FORM)).click()
        login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        name = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_PROFILE)).get_attribute("value")
        assert name == "Vasilia"

    def test_login_via_button_on_password_reset_form(self, driver):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PASSWORD_RESET_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_LINK_ON_REG_FORM)).click()
        login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        name = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_PROFILE)).get_attribute("value")
        assert name == "Vasilia"

    def test_logout(self, driver):
        driver.find_element(*TestLocators.LOGIN_IN_ACCOUNT_BUTTON).click()
        login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PREVIOUS_ORDERS))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        log = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_TEXT_AFTER_REG)).text
        assert log == "Вход"
