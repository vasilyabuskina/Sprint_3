from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators


class TestTransition:

    def test_transition_from_profile_to_constructor_via_click_on_constructor_button(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CONSTRUCTOR_BUTTON)).click()
        assemble = driver.find_element(*TestLocators.ASSEMBLE_BURGER).text
        assert assemble == "Соберите бургер"


    def test_transition_from_profile_to_constructor_via_click_on_stellar_burgers_logo(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.STELLAR_BURGERS_LOGO)).click()
        assemble = driver.find_element(*TestLocators.ASSEMBLE_BURGER).text
        assert assemble == "Соберите бургер"


    def test_transition_between_buns_sauces_fillings(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CONSTRUCTOR_BUTTON)).click()
        driver.find_element(*TestLocators.ASSEMBLE_BURGER)
        driver.find_element(*TestLocators.SAUCES).click()
        driver.find_element(*TestLocators.BUNS).click()
        driver.find_element(*TestLocators.FILLINGS).click()
        driver.find_element(*TestLocators.BUNS).click()
        driver.find_element(*TestLocators.FILLINGS).click()
        driver.find_element(*TestLocators.SAUCES).click()
        driver.find_element(*TestLocators.FILLINGS).click()
        beef = driver.find_element(*TestLocators.BEEF_METEORITE).text
        assert beef == "Говяжий метеорит (отбивная)"
