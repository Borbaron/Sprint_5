from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import Credentials

class TestGoToConstructorByButton:
    
    def test_go_to_constructor_by_button(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)

        driver.find_element(*Locators.ENTER_BUTTON).click()
<<<<<<< HEAD
=======
        #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
>>>>>>> 1508318b48aaa2abe7f79a16f44b41e76e868bd5
        driver.find_element(*Locators.KABINET_BUTTON).click()

        driver.find_element(*Locators.CONSTRUCT_BUT).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        assert order_button.is_displayed()

class TestGoToConstructorByLogon:
    
    def test_go_to_constructor_by_logo(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)

        driver.find_element(*Locators.ENTER_BUTTON).click()
<<<<<<< HEAD
=======
        #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
>>>>>>> 1508318b48aaa2abe7f79a16f44b41e76e868bd5
        driver.find_element(*Locators.KABINET_BUTTON).click()

        driver.find_element(*Locators.LOGO).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        assert order_button.is_displayed()