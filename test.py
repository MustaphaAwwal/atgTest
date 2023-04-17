import unittest

import collections
collections.Callable = collections.abc.Callable

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test_ATGWorld(unittest.TestCase):
	def setUp(self):
		self.chrome_options = Options()
		
		self.chrome_options.add_argument('--no-sandbox')
		self.chrome_options.add_argument('--disable-setuid-sandbox')
		self.driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=self.chrome_options)

	def test_atg_website(self):
		self.driver.get("https://atg.world/")
		print('Testing the page title')
		self.assertEqual(self.driver.title, "Across The Globe (ATG) - Professional and Personal Social Networking", 'wrong page title')
		print("Testing for page content using h2 element CSS_SELECTOR")
		self.assertTrue(  WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "h2"))
			), 'h2 element not present')
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
