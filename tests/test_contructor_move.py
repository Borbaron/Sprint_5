from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import Credentials

class TestGoToConstructorBuns:
    
    def test_go_to_buns_in_constructor(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SAUCES_BUTTON_ACTIVE)))
        driver.find_element(*Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.BUNS_BUTTON_ACTIVE)))

        buns_button_element = driver.find_element(*Locators.BUNS_BUTTON_ACTIVE)
        assert buns_button_element.is_displayed()

class TestGoToConstructorSauces:
    
    def test_go_to_sauces_in_constructor(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SAUCES_BUTTON_ACTIVE)))

        sauces_button_element = driver.find_element(*Locators.SAUCES_BUTTON_ACTIVE)
        assert sauces_button_element.is_displayed()

class TestGoToConstructorToppings:
    
    def test_go_to_toppings_in_constructor(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.TOPPINGS_BUTTON_ACTIVE)))

        toppings_button_element = driver.find_element(*Locators.TOPPINGS_BUTTON_ACTIVE)
        assert toppings_button_element.is_displayed()

