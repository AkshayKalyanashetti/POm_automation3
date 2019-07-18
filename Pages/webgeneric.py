from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators
class WebGeneric(Locators):
    def __init__(self, driver):
        Locators.__init__(self, driver)
        self.driver=driver
        self.lc=Locators(self.driver)

    def enter(self, locator_val, input_val):
        self.lc.driver.find_element_by_id(locator_val).send_keys(input_val)

    def enter(self, locator_val, input_val):

        self.lc.driver.find_element_by_name(locator_val).send_keys(input_val)

    def text(self, locator_val, input_val):
        self.lc.driver.find_element_by_xpath(locator_val).send_keys(input_val)

    def submit(self, locator_val):
        #wait = WebDriverWait(self.driver, 40)
        # self.driver.find_element_by_id(locator).click()
        #var = self.locator(locator_val)
        #var = wait.until(EC.element_to_be_clickable(locator_val))
        #var.click()
        self.lc.driver.find_element_by_xpath(locator_val).click()

