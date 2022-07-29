from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import regex as re
import emoji
from emoji import emojize
from selenium.webdriver.common.by import By

ROOT_DIR = os.path.abspath(os.curdir)
ser= Service(ROOT_DIR+'\Driver\chromedriver.exe')
gd = (ROOT_DIR+'\Driver\chromedriver.exe')
# print(ROOT_DIR+'\Driver\chromedriver.exe')
driver = webdriver.Chrome(service= ser)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = '"Ayisha"'

# Replace the below string with your own message
string =  "I love u very much baby" + ":-*" # "I Love you Baby" # :-)* or :-* or :-^ or ^>^

x_arg = '//span[contains(@title,' + target + ')]'
# print(x_arg)
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()
# print("click")
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'
input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))
# print("ele pre" + inp_xpath)
for i in range(10):
	input_box.send_keys(string + Keys.ENTER)
	time.sleep(0.4)
print("Message Sent")


colu_click = '//div[contains(@title,"Menu")]'
input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, colu_click)))
input_box.click()

log_out = '//div[text()="Log out"]'
#log_out =  '//div[contains(@aria-label,"Log out")]'
input_box2 = wait.until(EC.presence_of_element_located((
	By.XPATH, log_out)))
input_box2.click()
print("Logged out WA")
time.sleep(1)

# log_l = driver.find_element(By.XPATH, log_out2) # driver.find_elements_by_xpath("//div[text()='Log out']")
# text_length = log_l.is_displayed()
wait.until(EC.visibility_of_element_located((By.XPATH,log_out)));
if (driver.find_element(By.XPATH, log_out).is_displayed() == True):
   # m= log_l.text
   input_logof = wait.until(EC.presence_of_element_located((By.XPATH, log_out)))
   input_logof.click()
   print("Log out from WA")
   driver.quit()
else:
	driver.quit()
	print("Not found")
