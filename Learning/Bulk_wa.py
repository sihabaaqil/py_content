from datetime import datetime
import time
from httpx import options
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\Dell\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')
ROOT_DIR = os.path.abspath(os.curdir)

phoneNumber = int(input("Enter a phone Number :- ")) #input("Enter a Saved Name :- ")
message = input("Enter your message :- ")
count = int(input("Enter your count :- "))

now = datetime.now()
currentDate = now.strftime("%d-%m-%y %H-%M")
print("Current date and time :- ", currentDate)

userDate = input("Enter date time in Format(dd-mm-yyyy hh-mm) or current DateTime to type 1 :- ")
if(userDate=="1"):
    userDate = currentDate
else:
    pass
print(userDate)


while True:
    now = datetime.now()
    currentDate = now.strftime("%d-%m-%y %H-%M")
    if(userDate == currentDate):
        # driver = webdriver.Chrome('./chromedriver', options=options)
        ser = Service(ROOT_DIR + '\Driver\chromedriver.exe')
        driver = webdriver.Chrome(service=ser)
        driver.get("https://web.whatsapp.com/")
        time.sleep(30)

        print("\nStart\n")

        searchIcon = driver.find_element(By.CLASS_NAME, "_28-cz").click()
        print("1. Click on Search Icon")
        time.sleep(5)

        searchNewChat = driver.find_element(By.CLASS_NAME, "_13NKt")
        searchNewChat.send_keys(phoneNumber)
        print("2. send_keys in Search or start new chat")
        time.sleep(5)

        firstName = driver.find_element(By.CLASS_NAME, "_3m_Xw").click()
        print("3. Click on first chat")
        time.sleep(5)

        for i in range(0, count):
            msgSendKey = driver.find_elements(By.CLASS_NAME, "_13NKt")[1]
            msgSendKey.send_keys(message)
            print("4. send_keys in Type a message")
            time.sleep(5)

            sendButton = driver.find_element(By.CLASS_NAME, "_4sWnG").click()
            print("5. Click on send button")
            time.sleep(5)

        driver.close()
        sys.exit()

print("\nEnd\n")