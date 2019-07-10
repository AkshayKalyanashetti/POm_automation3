class Locators:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, locator_type, locator_val):
        try:
            if (locator_type == "id"):
                ele = self.driver.find_element_by_id(locator_val)
            elif (locator_type == "name"):
                ele = self.driver.find_element_by_name(locator_val)
            elif (locator_type == "xpath"):
                ele = self.driver.find_element_by_xpath(locator_val)

        except:
            print('execption handling')