from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Chrome('./chromedriver')


driver.get("https://six-guys.github.io/")

home_btn = driver.find_element_by_xpath("/html/body/div[1]/a[2]")

driver.implicitly_wait
home_btn.click()







#driver.close()

