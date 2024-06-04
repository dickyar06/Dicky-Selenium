import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class DemoWeb(unittest.TestCase):

    def setUp(self):
        self.browser  = webdriver.Chrome()

    def test_register(self):
        browser = self.browser

        browser.get('https://demowebshop.tricentis.com/register')
        self.assertIn('Register', self.browser.title)
        
        



if __name__ == "__main__":
    unittest.main()