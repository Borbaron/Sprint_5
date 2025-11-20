from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import Credentials

class TestLogout:
    
    def test_logout_from_profile(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        driver.find_element(*Locators.KABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.EXIT_BUTTON)))
        driver.find_element(*Locators.EXIT_BUTTON).click()

        
        enter_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ENTER_TEXT)))
        assert enter_text.is_displayed()