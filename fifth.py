#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def seleniumPageLoad():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=chrome_options)
    driver.get("https://atg.world")
    try:
        ele = WebDriverWait(driver, 10).until( #using explicit wait for 10 seconds
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2")) #checking for the element with 'h2'as its CSS
    )
        print("Page is loaded within 10 seconds.")
    except:
        print("Timeout Exception: Page did not load within 10 seconds.")
#driver
if __name__ == "__main__":
    seleniumPageLoad() #call the function

