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
		
		self.chrome_options.switches="""--start-maximized;--test-type;--no-sandbox;--ignore-certificate-errors;
                   --disable-popup-blocking;--disable-default-apps;--disable-extensions-file-access-check;
                   --incognito;--disable-infobars,--disable-gpu"""
		
		WebDriverManager.chromedriver().setup();
ChromeOptions options = new ChromeOptions();
options.addArguments("--window-size=1920,1080");
options.addArguments("--allow-insecure-localhost");
options.addArguments("--headless");
options.addArguments();
options.addArguments("");
options.addArguments("--ignore-certificate-errors");
options.addArguments("--allow-running-insecure-content");
options.addArguments("--disable-setuid-sandbox");
options.addArguments("--disable-dev-shm-usage");
driver = new ChromeDriver(options);
DriverManager.setDriver(driver);
		self.chrome_options.add_argument('--window-size=1920,1080')
		self.chrome_options.add_argument('--allow-insecure-localhost')
		self.chrome_options.add_argument('--headless')
		self.chrome_options.add_argument('--disable-gpu')
		self.chrome_options.add_argument('--no-sandbox')
		self.chrome_options.add_argument('--ignore-certificate-errors')
		self.chrome_options.add_argument('--disable-dev-shm-usage')
		self.chrome_options.add_argument('--disable-dev-shm-usage')
		self.driver = webdriver.Chrome(service=Service('./chromedriver'), options=self.chrome_options)

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
