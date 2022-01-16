from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


#run using cmd; type py -m unittest Eyeroh_tests.py
class EyerohIndexPageTest(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        cls.driver = webdriver.Chrome('./chromedriver')
        cls.driver.implicitly_wait(10)
        
    def test_click_team_button(self):
        self.home_btn = self.driver.find_element_by_xpath("/html/body/div[1]/a[2]")
        self.home_btn.click()

    def test_navigate_to_contact_page(self):
        self.contact_button = self.driver.find_element_by_name("Contact")
        self.contact_button.click()

    def tearDown(self):
        self.driver.get("https://six-guys.github.io/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


