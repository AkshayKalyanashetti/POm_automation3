#from TestData.data import *
from Pages.webgeneric import WebGeneric
class HomeTime:
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.user_id = 'username'
        self.pass_name = 'pwd'

    def homescreen(self):
        wg = WebGeneric(self.driver)
        wg.submit("//a[text()='View Time-Track']")
        wg.submit("//a[text()='Lock Time-Track']")
