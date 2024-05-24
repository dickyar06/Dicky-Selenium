from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://demowebshop.tricentis.com/login')
browser.find_element(By.NAME,'Email').send_keys('dicky123@gmail.com')
browser.find_element(By.NAME,'Password').send_keys('123456789')
browser.find_element(By.CSS_SELECTOR,'.button-1.login-button').click()
browser.find_element(By.CSS_SELECTOR,'input.button-2.product-box-add-to-cart-button').click()
browser.find_element(By.ID, 'giftcard_2_RecipientName').send_keys('Dicky Rachman')
browser.find_element(By.ID,'giftcard_2_RecipientEmail').send_keys('dicky123@gmail.com')