#!/usr/bin/python3
#Importing necessary libraries


from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver_location = "/usr/bin/google-chrome"
binary_location = "/usr/bin/chromedriver"
#wait for page load function
def seleniumPageLoad():
    #creating a webdriver object
    option = Options()
    option.binary_location = binary_location
    option.add_argument("headless");
   # option.add_argument('--no-sandbox')
   # option.add_argument('--disable-dev-shm-usage')
#    chromeOptions.setHeadless(true)

#    System.setProperty("webdriver.chrome.driver", "/usr/bin/chromedriver")
#    WebDriver driver = new ChromeDriver(chromeOptions)
    driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=option)
#    driver.maximize_window() #maximize window size
    driver.get("https://atg.world/") #opening the url
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
