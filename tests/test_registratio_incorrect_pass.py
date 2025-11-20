from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators

class TestRegistrationWrongPass:
    
    def test_wrong_pass_registration(self, driver):
        driver.find_element(*Locators.KABINET_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        email = generate_registration_data()
        driver.find_element(*Locators.REG_NAME).send_keys("Анатолий")
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASS).send_keys("QWE")

        driver.find_element(*Locators.REG_BUTTON).click()

<<<<<<< HEAD
        error_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INCORRECT_PASS)))
=======
        error_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ENTER_TEXT)))
>>>>>>> 1508318b48aaa2abe7f79a16f44b41e76e868bd5
        assert error_element.is_displayed()