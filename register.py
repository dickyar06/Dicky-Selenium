from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://demowebshop.tricentis.com/register')
browser.find_element(By.CSS_SELECTOR,'input#gender-male').click()
browser.find_element(By.NAME,'FirstName').send_keys('Dicky')
browser.find_element(By.NAME,'LastName').send_keys('Rachman')
browser.find_element(By.NAME,'Email').send_keys('dicky123@gmail.com')
browser.find_element(By.NAME,'Password').send_keys('123456789')
browser.find_element(By.NAME,'ConfirmPassword').send_keys('123456789')
browser.find_element(By.NAME,'register-button').click()