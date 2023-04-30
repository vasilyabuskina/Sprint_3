from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators

class TestLogin:

#функция - заполнение полей входа
    def login_fields_form(self, driver):
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_LOGIN_FORM).send_keys('vasilia_buskina_08_123@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_LOGIN_FORM).send_keys('yandex123')
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

#вход через кнопку Войти в аккаунт
    def test_login_via_login_in_account_button(self, driver):
        driver.find_element(*TestLocators.LOGIN_IN_ACCOUNT_BUTTON).click() #LOGIN_IN_ACCOUNT_BUTTON
        self.login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Vasilia']")))
        #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]"))).click()

        assert True

#вход через кнопку Личный Кабинет
    def test_login_via_profile_button(self, driver):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()#PROFILE_BUTTON
        self.login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Vasilia']")))
        #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]"))).click()
        assert True

#вход через форму регистрации
    def test_login_via_button_on_registration_form(self, driver):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_LINK)).click()#REGISTRATION_LINK
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_LINK_ON_REG_FORM))).click()#LOGIN_BUTTON
        self.login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Vasilia']")))
        #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]"))).click()
        assert True

#вход через форму восстановления пароля
    def test_login_via_button_on_password_reset_form(self, driver):
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PASSWORD_RESET_BUTTON))).click()#PASSWORD_RESET_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGIN_LINK_ON_REG_FORM))).click()#LOGIN_BUTTON
        self.login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Vasilia']")))
        #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]"))).click()
        assert True

#проверка выхода
    def test_logout(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        self.login_fields_form(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Vasilia']")))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.LOGOUT_BUTTON))).click()#LOGOUT_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until_not(EC.visibility_of_element_located((By.XPATH, "//input[@value='Vasilia']")))
        assert True



