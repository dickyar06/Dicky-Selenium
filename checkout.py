import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class demowebshopTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def test_login(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/login')
        self.assertIn('Demo Web Shop', self.browser.title)
        browser.find_element(By.NAME,'Email').send_keys('dicky123@gmail.com')
        browser.find_element(By.NAME,'Password').send_keys('123456789')
        browser.find_element(By.CSS_SELECTOR,'.button-1.login-button').click()
        browser.find_element(By.CSS_SELECTOR,'div:nth-of-type(3) > .product-item input[value="Add to cart"]').click()
        browser.find_element(By.CSS_SELECTOR,'li#topcartlink  .cart-label').click()
        
        browser.find_element(By.XPATH,'//input[@id="termsofservice"]').click()
        browser.find_element(By.XPATH,'//button[@id="checkout"]').click()

        browser.find_element(By.XPATH,'//input[@id="BillingNewAddress_FirstName"]').send_keys('dinda')
        browser.find_element(By.XPATH,'//input[@id="BillingNewAddress_LastName"]').send_keys('intan')
        browser.find_element(By.XPATH,'//input[@id="BillingNewAddress_Email"]').send_keys('intandinda@gmail.com')
        browser.find_element(By.NAME,'BillingNewAddress.Company').send_keys('warkodjan')
        browser.find_element(By.NAME,'BillingNewAddress.City').send_keys('bandung')
        browser.find_element(By.NAME,'BillingNewAddress.Address1').send_keys('bandung jawabarat')
        browser.find_element(By.NAME,'BillingNewAddress.CountryId').send_keys('indonesia')
        browser.find_element(By.NAME,'BillingNewAddress.ZipPostalCode').send_keys('40233')
        browser.find_element(By.NAME,'BillingNewAddress.PhoneNumber').send_keys('081233477909')
        
        browser.find_element(By.XPATH,'//body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[1]/div[2]/div[1]/input[1]').click()
        browser.find_element(By.XPATH,'//body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[2]/div[2]/div[1]/input[1]').click()

        browser.find_element(By.XPATH,'//input[@id="shippingoption_1"]').click()
        browser.find_element(By.XPATH,'//body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[3]/div[2]/form[1]/div[2]/input[1]').click()

        browser.find_element(By.CSS_SELECTOR,'#paymentmethod_0').click()
        browser.find_element(By.XPATH,'//body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[4]/div[2]/div[1]/input[1]').click()

        browser.find_element(By.XPATH,'//body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[4]/div[2]/div[1]/input[1]').click()

        browser.find_element(By.XPATH,'//body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[6]/div[2]/div[2]/input[1]').click()
       
        browser.find_element(By.XPATH,'//body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[6]/div[2]/div[2]/input[1]').click()
        webdriver.Chrome().close

if __name__ == '__main__':
    unittest.main()