from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.firefox()
browser.get('https://demowebshop.tricentis.com/login')
browser.find_element(by.NAME,'name')