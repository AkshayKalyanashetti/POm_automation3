from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:/Users/Akshay/Downloads/chrome/chromedriver")
driver.get('https://google.com')
driver.get('https://demo.actitime.com')
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_name('pwd').send_keys('manager')
#driver.find_element_by_xpath("//div[text()='Login ']").click()  #//a[text()='View Time-Track']

wait = WebDriverWait(driver, 10)
#self.driver.find_element_by_id(locator).click()
# var = self.locator(locator_type, locator_val)
status = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Login ']")))
status.click()
print(status)