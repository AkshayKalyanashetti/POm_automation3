from Pages.webgeneric import WebGeneric
class HomeScreen:
    def __init__(self,driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
    def logout(self):
        wg = WebGeneric(self.driver)
        wg.submit('//*[@id="logoutLink"]')
        print("logout Passed")
        #self.driver.find_element_by_id('logoutLink').click()