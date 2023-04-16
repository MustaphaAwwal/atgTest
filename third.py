#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.python.org/")
time.sleep(2)
search_box = driver.find_element(By.ID, 'id-search-field')
search_box.send_keys('selenium')
search_box.submit()
time.sleep(2)
driver.close()
