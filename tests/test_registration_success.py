from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators

class TestRegistrationSuccess:

    def test_sucsess_registration(self, driver):
        driver.find_element(*Locators.KABINET_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        email, password = generate_registration_data()
        driver.find_element(*Locators.REG_NAME).send_keys("Анатолий")
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASS).send_keys(password)
                            
        driver.find_element(*Locators.REG_BUTTON).click()

        vhod = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ENTER_TEXT))
        assert vhod.is_displayed()

