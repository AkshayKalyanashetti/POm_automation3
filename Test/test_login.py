from Pages.login import *
from Pages.homepage import *
from Pages.task import TaskScreen
import pytest
@pytest.mark.usefixtures('pre_and_post_action')
class Test_login:
    def test_actitime(self):
        driver= self.driver
        lp = LoginPage(driver)
        lp.actilogin()

    def test_task(self):
        driver = self.driver
        lp = TaskScreen(driver)
        lp.task()

    def test_logout(self):
        driver = self.driver
        lout=HomeScreen(driver)
        lout.logout()

#def test_logout():
#    driver.find_element_by_id('logoutLink').click()