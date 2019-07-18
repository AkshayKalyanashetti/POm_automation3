from Pages.webgeneric import WebGeneric
class TaskScreen:
    def __init__(self,driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.user_name = '//input[@class="inputFieldWithPlaceholder newNameField inputNameField"]'
        self.user_descrip = "//textarea[@placeholder='Enter Customer Description']"


    def task(self):
        wg = WebGeneric(self.driver)
        wg.submit('//*[@id="topnav"]/tbody/tr[1]/td[3]/a/div[1]')
        wg.submit('//div[text()="Add New"]')
        wg.submit("//div[text()='+ New Customer']")
        wg.text(self.user_name, 'Akshay121')
        wg.text(self.user_descrip, 'good one11')
        wg.submit("//div[@class='emptySelection']")
        wg.submit('//*[@id="customerLightBox_content"]/div[3]/div[2]/div[2]')
        import time
        time.sleep(5) #manually click on OK button when javascript pop-up comes on the screen
        print('Passed')