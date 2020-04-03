from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class WebLogin:
    def __init__(self, driver, url, credential):
        self.driver = driver
        self.url = url
        self.credential = credential

    def messier_login(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "user")))

        self.driver.find_element_by_id('user').send_keys(self.credential['username'])
        self.driver.find_element_by_id('pass').send_keys(self.credential['password'])
        self.driver.find_element_by_id('logon').send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "Home_logoBox")))

    def hc_login(self):
        print("HC Login")
