#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=chrome_options)
#d.get('https://www.google.nl/')

d.get("https://atg.world/") #opening the url
print(d.title)

