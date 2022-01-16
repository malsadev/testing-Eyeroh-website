from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest



class EyerohIndexPageTest(unittest.TestCase):

    def setupClass(cls):
        cls.driver = webdriver.Chrome('./chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        driver.get("https://six-guys.github.io/")


    def test_click_team_button(self):
        self.home_btn = driver.find_element_by_xpath("/html/body/div[1]/a[2]")
        self.home_btn.click()

    def test_navigate_to_contact_page(self):
        self.contact_button = driver.find_element_by_name("Contact")
        self.contact_button.click()





driver = webdriver.Chrome('./chromedriver')


driver.get("https://six-guys.github.io/")

home_btn = driver.find_element_by_xpath("/html/body/div[1]/a[2]")

driver.implicitly_wait
home_btn.click()







#driver.close()

