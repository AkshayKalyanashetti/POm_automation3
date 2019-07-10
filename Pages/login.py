from TestData.data import *
from Pages.webgeneric import WebGeneric
class LoginPage:
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.user_id = 'username'
        self.pass_name = 'pwd'
        self.login_xpath = "//div[text()='Login ']"

    def actilogin(self):
        wg = WebGeneric(self.driver)
        wg.enter(self.user_id, USERNAME)
        wg.enter(self.pass_name, PASSWORD)
        wg.submit(self.login_xpath)
