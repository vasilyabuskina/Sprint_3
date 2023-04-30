from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators


faker = Faker()
class TestRegistration:
    def test_reg_success(self, driver):
        email = faker.email()
        # print(email)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()#REGISTRATION
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_REG_FORM)).send_keys('Vasilia')#NAME_FIELD_IN_REG_FORM
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REG_FORM).send_keys(email)#EMAIL_FIELD_IN_REG_FORM
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REG_FORM).send_keys('yandex123')#PASSWORD_FIELD_IN_REG_FORM
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()#REGISTRATION_BUTTON
        # проверка есть ли зарегистрированный пользователь
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON)).click() #LOGIN_BUTTON
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_LOGIN_FORM).send_keys(email) #EMAIL_FIELD_IN_LOGIN_FORM
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_LOGIN_FORM).send_keys('yandex123') #PASSWORD_FIELD_IN_LOGIN_FORM
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON)).click() #LOGIN_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Vasilia']")))
        assert True

    def test_reg_five_symbols_password_shows_error(self, driver):
        email = faker.email()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()#REGISTRATION_LINK
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_REG_FORM)).send_keys('Vasilia')#NAME_FIELD_IN_REG_FORM
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REG_FORM).send_keys(email)#EMAIL_FIELD_IN_REG_FORM
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REG_FORM).send_keys('yand1')#PASSWORD_FIELD_IN_REG_FORM
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON)).click()#REGISTRATION_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.WRONG_PASSWORD))#WRONG_PASSWORD
        assert True

    def test_reg_empty_name_did_not_registered(self,driver):
        email = faker.email()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()#REGISTRATION_lINK
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.NAME_FIELD_IN_REG_FORM)).send_keys()#NAME_FIELD_IN_REG_FORM
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REG_FORM).send_keys(email)#EMAIL_FIELD_IN_REG_FORM
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REG_FORM).send_keys('yandex1')#PASSWORD_FIELD_IN_REG_FORM
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON)).click()
        WebDriverWait(driver, 3).until_not(EC.visibility_of_element_located(TestLocators.LOGIN_TEXT_AFTER_REG))
        assert True


#другой вариант написания
    def test_reg_five_symbols_password_shows_error2(self, driver, findw, find):
        email = faker.email()
        # print(email)
        findw(TestLocators.PROFILE_BUTTON).click()
        findw(TestLocators.REGISTRATION_LINK).click()  # REGISTRATION_BUTTON
        findw(TestLocators.NAME_FIELD_IN_REG_FORM).send_keys('Vasilia')  # NAME_FIELD_IN_REG_FORM
        findw(TestLocators.EMAIL_FIELD_IN_REG_FORM).send_keys(email)  # EMAIL_FIELD_IN_REG_FORM
        findw(TestLocators.PASSWORD_FIELD_IN_REG_FORM).send_keys('yandex123')  # PASSWORD_FIELD_IN_REG_FORM
        findw(TestLocators.REGISTRATION_BUTTON).click()
        # проверка есть ли зарегистрированный пользователь
        findw(TestLocators.LOGIN_BUTTON).click()  # LOGIN_BUTTON
        findw(TestLocators.EMAIL_FIELD_IN_LOGIN_FORM).send_keys(email)  # EMAIL_FIELD_IN_LOGIN_FORM
        findw(TestLocators.PASSWORD_FIELD_IN_LOGIN_FORM).send_keys('yandex123')  # PASSWORD_FIELD_IN_LOGIN_FORM
        findw(TestLocators.LOGIN_BUTTON).click()  # LOGIN_BUTTON
        findw(TestLocators.PROFILE_BUTTON).click()  # PROFILE_BUTTON
        findw((By.XPATH, "//input[@value='Vasilia']"))

        assert True











