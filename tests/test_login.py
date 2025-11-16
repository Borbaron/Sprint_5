from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators
from data import Credentials

class TestVoitivAccauntButton:
    
    def test_login_from_acc_button(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        assert order_button.is_displayed()

class TestLichniyKabinetLogin:
    
    def test_login_from_profile(self, driver):
        driver.find_element(*Locators.KABINET_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        assert order_button.is_displayed()

class TestLoginFromRegistrationForm:
    
    def test_login_from_reg_form(self, driver):
        driver.find_element(*Locators.KABINET_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.ENT_LINK).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        assert order_button.is_displayed()

class TestLoginFromRecoverPass:
    
    def test_login_from_recover_pass(self, driver):
        driver.find_element(*Locators.KABINET_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASS).click()
        driver.find_element(*Locators.ENT_LINK).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        assert order_button.is_displayed()