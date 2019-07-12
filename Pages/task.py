from Pages.webgeneric import WebGeneric
class TaskScreen:
    def __init__(self,driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
    def task(self):
        wg = WebGeneric(self.driver)
        wg.submit('//*[@id="topnav"]/tbody/tr[1]/td[3]/a/div[1]')