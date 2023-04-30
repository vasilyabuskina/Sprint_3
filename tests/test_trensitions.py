from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators

class TestTransition:

#переход из личного кабинета в конструктор по клику на Конструктор
    def test_transition_from_profile_to_constructor_via_click_on_constructor_button(self,login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.CONSTRUCTOR_BUTTON))).click() #CONSTRUCTOR_BUTTON
        driver.find_element(*TestLocators.ASSEMBLE_BURGER)#ASSEMBLE_BURGER
        assert True

#переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_transition_from_profile_to_constructor_via_click_on_stellar_burgers_logo(self,login):
        driver = login
        #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.STELLAR_BURGERS_LOGO))).click()#STELLAR_BURGERS_LOGO
        driver.find_element(*TestLocators.ASSEMBLE_BURGER)#ASSEMBLE_BURGER
        assert True

#переход между разделами Булки - Соусы - Начинки
    def test_transition_betwin_buns_sauces_fillings(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.PROFILE_BUTTON))).click()#PROFILE_BUTTON
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((TestLocators.CONSTRUCTOR_BUTTON))).click()#CONSTRUCTOR_BUTTON
        driver.find_element(*TestLocators.ASSEMBLE_BURGER)#ASSEMBLE_BURGER
        driver.find_element(*TestLocators.SAUCES).click()#SAUCES
        driver.find_element(*TestLocators.BUNS).click()#BUNS
        driver.find_element(*TestLocators.FILLINGS).click()#FILLINGS
        driver.find_element(*TestLocators.BUNS).click()#BUNS
        driver.find_element(*TestLocators.FILLINGS).click()#FILLINGS
        driver.find_element(*TestLocators.SAUCES).click()#SAUCES
        driver.find_element(*TestLocators.FILLINGS).click()#FILLINGS
        assert True
