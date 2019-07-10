class HomeScreen:
    def __init__(self,driver):
        self.driver = driver
    def logout(self):
        self.driver.find_element_by_id('logoutLink').click()