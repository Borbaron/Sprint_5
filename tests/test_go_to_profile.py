from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import Credentials

class TestGoToProfileFromButton:
    
    def test_go_to_profile_from_login_button(self, driver):
        driver.find_element(*Locators.VOITI_V_ACCAUNT_BUTTON).click()

        driver.find_element(*Locators.ENT_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.ENT_PASS).send_keys(Credentials.password)

        driver.find_element(*Locators.ENTER_BUTTON).click()
        #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.ORDER_BUTTON)))
        driver.find_element(*Locators.KABINET_BUTTON).click()

        history_link = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.HISTORY_LINK)))
        assert history_link.is_displayed()