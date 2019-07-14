from Pages.webgeneric import WebGeneric
from TestData.data import *
class UserScreen:
    def __init__(self,driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.user_name = 'firstName'
        #self.pass_name = 'pwd'

    def user(self):
        wg = WebGeneric(self.driver)
        wg.submit('//*[@id="topnav"]/tbody/tr/td[5]/a/div[1]')
        wg.submit('//*[@id="pageBody"]/tbody/tr[1]/td[3]/div/div[3]')
        wg.enter(self.user_name, NAME)