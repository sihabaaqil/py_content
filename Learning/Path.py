import time
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service

ROOT_DIR = os.path.abspath(os.curdir)
print("Path :"+ROOT_DIR)
ser= Service(ROOT_DIR+'\Driver\chromedriver.exe')
driver = webdriver.Chrome(service= ser)
driver.get("https://www.google.com/") #  https://web.whatsapp.com/