# Global Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('./chromedriver')
driver.get("https://interaksyon.philstar.com/trends-spotlights/2020/05/20/168896/francis-leo-marcos-profile-norman-mangusin/")

str = driver.find_element_by_xpath('//*[@id="post-168896"]/div[1]/header/h1').text
print(str)

str = driver.find_element_by_xpath('//*[@id="post-168896"]/div[1]/header/h1').text
print(str[10:])



