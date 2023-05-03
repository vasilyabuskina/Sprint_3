from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators


faker = Faker()
class TestRegistration:
    def test_reg_success(self, driver):
        email = faker.email()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_REG_FORM)).send_keys('Vasilia')
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REG_FORM).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REG_FORM).send_keys('yandex123')
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON)).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_LOGIN_FORM).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_LOGIN_FORM).send_keys('yandex123')
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        name = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_PROFILE)).get_attribute("value")
        assert name == "Vasilia"


    def test_reg_five_symbols_password_shows_error(self, driver):
        email = faker.email()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_REG_FORM)).send_keys('Vasilia')
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REG_FORM).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REG_FORM).send_keys('yand1')
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON)).click()
        wrong = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.WRONG_PASSWORD)).text
        assert wrong == "Некорректный пароль"

    def test_registration_empty_name_did_not_registered(self,driver):
        email = faker.email()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_REG_FORM)).send_keys()
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REG_FORM).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REG_FORM).send_keys('yandex1')
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON)).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"
