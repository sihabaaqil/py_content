from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from CommonUtilities import my_function
from DB import db_connection as connect
from DB import get_url
from DB import get_cta_locators

# Read inputs from excel
# Env = QA, Brand = CrepeERase, Campaign = core

# url = get_url (env, brand, campaign)
# url ="https:// www.crepeerase.com"
data = my_function()
for x in data:
    print(x)
    if x[0] == "Environment":
        continue
    elif x[0] == "End":
        break
    else:
        env = x[0]
        brand = x[1]
        campaign = x[2]
        print("Execution started for " + env + brand + campaign)
        URL = get_url(env, brand, campaign)
        print(URL)
        driver = webdriver.Chrome(executable_path=r"F:\Python\GR\Driver\chromedriver.exe")
        driver.maximize_window()
        driver.get(URL)
        # Step 1 : Check - Terms & Conditions
        # Store all locators in content_locators table
        # Replicate get_element_locator function from CommonUtilities.java file
        print(driver.title)
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Terms & Conditions')]")))
        TC = driver.find_element_by_xpath("//a[contains(text(),'Terms & Conditions')]")
        TC.click()
        TC1 = "//div[@id='popupcontent']"
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, TC1)))
        element1 = driver.find_element_by_xpath("//div[@id='popupcontent']").text
        element2 = element1.rstrip()
        path = "F:\Python\GR\Content\Terms of Use and Conditions\English"
        path2 = path + "\\" + brand + ".txt"
        File2 = open(path2, "r")
        File1 = (File2.read())
        File1.rstrip()
        if (element2 == File1):
            print("Terms of Use and Conditions of Purchase : " + "Passed")
        else:
            print("Terms of Use and Conditions of Purchase : " + "Failed")

        # Step 2 : Check - Sales Tax link

        element3 = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Sales Tax')]")))
        TC4 = driver.find_element_by_xpath("//a[contains(text(),'Sales Tax')]")
        TC4.click()

        try:
            element9 = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'Sales Tax')]")))
            print("Sales Tax : " + "Passed")
        except NoSuchElementException:
            print("Sales Tax link not found : " + "Failed")

        time.sleep(5)

        # Step 3 : Check - Privacy Policy
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'Privacy Policy')]")))  # //a[contains(text(),'Privacy Policy')]
        TC3 = driver.find_element_by_xpath("//*[contains(text(),'Privacy Policy')]")
        TC3.click()

        p = driver.current_window_handle
        chwd = driver.window_handles
        for w in chwd:
            # switch focus to child window
            if (w != p):
                driver.switch_to.window(w)
                break
                time.sleep(0.9)
                print("Child window title: " + driver.title)

        TC1 = "//h1[contains(text(),'Privacy Policy')]"
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, TC1)))
        element4 = driver.find_element_by_xpath("//div[@id='content']").text
        element5 = element4.rstrip()
        path = "F:\Python\GR\Content\Privacy Policy\English"
        path1 = path + "\\" + brand + ".txt"
        File3 = open(path1, "r")
        File4 = File3.read()
        File5 = File4.rstrip()
        if (element5 == File5):
            print("Privacy Policy : " + "Passed")
        else:
            print("Privacy Policy : " + "Failed")
            print(File5)
        time.sleep(5)
        element6 = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Your California Privacy Rights')]")))
        TC4 = driver.find_element_by_xpath("//a[contains(text(),'Your California Privacy Rights')]")
        TC4.click()

        try:
            element9 = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@id='Your_California_Privacy_Rights']")))
            print("Your California Privacy Rights : " + "Passed")
        except NoSuchElementException:
            print("Your California Privacy Rights link not found : " + "Failed")

        # Step 4 : Check - live chat & Phone number
        time.sleep(5)
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Customer Service')]")))
        TC4 = driver.find_element_by_xpath("//a[contains(text(),'Customer Service')]")
        TC4.click()

        driver.switch_to.window(driver.window_handles[2])
        if (brand == "CrepeErase"):
            element = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//span[contains(text(),'Click here')]")))  # //span[contains(text(),'Click here')]
            # //span[contains(text(),'Click here to reach us via live chat')]
            TC8 = driver.find_element_by_xpath("//span[contains(text(),'Click here')]")
            TC8.click()
            Number = driver.find_element_by_xpath("//div[@class='text-left']//p//a").is_displayed()
            if (Number == True):
                print("Number Displayed : " + "Passed")
            else:
                print("Number not found : " + "Failed")
            chat = driver.find_element_by_xpath(
                "//span[contains(text(),'Click here')]").is_displayed()
            if (chat == True):
                print("live chat : " + "Passed")
            else:
                print("live chat link not found : " + "Failed")
        elif (brand == "MeaningfulBeauty"):
            element = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//span[contains(text(),'Click here')]")))  # //span[contains(text(),'Click here')]
            # //span[contains(text(),'Click here to reach us via live chat')]
            TC8 = driver.find_element_by_xpath("//span[contains(text(),'Click here')]")
            TC8.click()
            Number = driver.find_element_by_xpath("//a[contains(text(),'(800)-927-0047')]").is_displayed()
            if (Number == True):
                print("Number Displayed : " + "Passed")
            else:
                print("Number not found : " + "Failed")
            chat = driver.find_element_by_xpath(
                "//span[contains(text(),'Click here')]").is_displayed()
            if (chat == True):
                print("live chat : " + "Passed")
            else:
                print("live chat link not found : " + "Failed")
        elif (brand == "WestmoreBeauty"):
            element = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//span[contains(text(),'Click here')]")))  # //span[contains(text(),'Click here')]
            # //span[contains(text(),'Click here to reach us via live chat')]
            TC8 = driver.find_element_by_xpath("//span[contains(text(),'Click here')]")
            TC8.click()
            Number = driver.find_element_by_xpath("//a[contains(text(),'888-366-3095')]").is_displayed()
            if (Number == True):
                print("Number Displayed : " + "Passed")
            else:
                print("Number not found : " + "Failed")
            chat = driver.find_element_by_xpath(
                "//span[contains(text(),'Click here')]").is_displayed()
            if (chat == True):
                print("live chat : " + "Passed")
            else:
                print("live chat link not found : " + "Failed")

        # Step 5 : Check - Do not sell my info link
        driver.switch_to.window(driver.window_handles[2])
        # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(URL)
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@id='donot-sell']")))
        donot_sell = driver.find_element_by_xpath("//a[@id='donot-sell']").is_displayed()
        if (donot_sell == True):
            print("Do Not Sell My Info in Home page Displayed : " + "Passed")
        else:
            print("Do Not Sell My Info in Home page link not found : " + "Failed")
        if (brand == "CrepeErase"):
            cta_locators = get_cta_locators(env, brand, campaign)
            element6 = driver.find_element_by_xpath(cta_locators).click()
            if (donot_sell == True):
                print("Do Not Sell My Info in SAS Displayed : " + "Passed")
            else:
                print("Do Not Sell My Info in SAS link not found : " + "Failed")
            try:
                kit_id = "//div[@data-productid='CSPG029']//div[@class='sas-checkbox clearfix']//h3"
                element13 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, kit_id)))
                element12 = driver.find_element_by_xpath(
                    kit_id).click()
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                element9 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//a[@class='cta']")))
                element10 = driver.find_element_by_xpath("//a[@class='cta']").click()
                # Step 6 : Check - T&C Popup link functionality on checkout page
                TC_PU = "//*[@id='tncEntryKit']/p/span[1]/a"
                element9 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='tncEntryKit']/p/span[1]/a")))
                element10 = driver.find_element_by_xpath("//*[@id='tncEntryKit']/p/span[1]/a").click()
                element13 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='popupRevealModal']/div[2]/button")))
                TC_PU_Cs = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").is_displayed()
                element14 = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").click()
                if (TC_PU_Cs == True):
                    print("T&C Popup link in Checkout Displayed : " + "Passed")
                else:
                    print("T&C Popup link in Checkout link not found : " + "Failed")
            except NoSuchElementException:
                element11 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[@class='button checkout']")))
                element12 = driver.find_element_by_xpath("//button[@class='button checkout']").click()
            if (donot_sell == True):
                print("Do Not Sell My Info in Checkout Displayed : " + "Passed")
            else:
                print("Do Not Sell My Info in Checkout link not found : " + "Failed")

        elif (brand == "MeaningfulBeauty"):
            cta_locators = get_cta_locators(env, brand, campaign)
            element6 = driver.find_element_by_xpath(cta_locators).click()
            if (donot_sell == True):
                print("Do Not Sell My Info in SAS Displayed : " + "Passed")
            else:
                print("Do Not Sell My Info in SAS link not found : " + "Failed")
            try:
                check_out = "//strong[contains(text(),'PROCEED TO CHECKOUT')]"
                element13 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, check_out)))
                element12 = driver.find_element_by_xpath(
                    check_out).click()
                TC_PU = "//*[@id='tncEntryKit']/p/nobr/a"

                element9 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='tncEntryKit']/p/nobr/a")))
                element10 = driver.find_element_by_xpath("//*[@id='tncEntryKit']/p/nobr/a").click()
                element13 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='popupRevealModal']/div[2]/button")))
                TC_PU_Cs = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").is_displayed()
                element14 = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").click()

                if (TC_PU_Cs == True):
                    print("T&C Popup link in Checkout Displayed : " + "Passed")
                else:
                    print("T&C Popup link in Checkout link not found : " + "Failed")
            except NoSuchElementException:
                element11 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[@class='button checkout']")))
                element12 = driver.find_element_by_xpath("//button[@class='button checkout']").click()
            if (donot_sell == True):
                print("Do Not Sell My Info in Checkout Displayed : " + "Passed")
            else:
                print("Do Not Sell My Info in Checkout link not found : " + "Failed")
        else:  # WestmoreBeauty
            cta_locators = get_cta_locators(env, brand, campaign)
            element6 = driver.find_element_by_xpath(cta_locators).click()
            if (donot_sell == True):
                print("Do Not Sell My Info in SAS Displayed : " + "Passed")
            else:
                print("Do Not Sell My Info in SAS link not found : " + "Failed")
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[2])
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            kit_id = "//button[@id='valuePack-next-btn']"
            element13 = WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located((By.XPATH, kit_id)))
            element12 = driver.find_element_by_xpath(kit_id).click()
            try:
                Thanks = "//button[contains(text(),'No, Thanks')]"
                element18 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, Thanks)))
                upgrade_dis = driver.find_element_by_xpath(Thanks).is_displayed()
                if (upgrade_dis == True):
                    element16 = driver.find_element_by_xpath(Thanks).click()
                if (donot_sell == True):
                    print("Do Not Sell My Info in Checkout Displayed : " + "Passed")
                else:
                    print("Do Not Sell My Info in Checkout link not found : " + "Failed")
                TC_PU = "//*[@id='tncEntryKit']/p/nobr/a"

                element9 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='tncEntryKit']/p/nobr/a")))
                element10 = driver.find_element_by_xpath("//*[@id='tncEntryKit']/p/nobr/a").click()
                element13 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='popupRevealModal']/div[2]/button")))
                TC_PU_Cs = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").is_displayed()
                element14 = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").click()
                if (TC_PU_Cs == True):
                    print("T&C Popup link in Checkout Displayed : " + "Passed")
                else:
                    print("T&C Popup link in Checkout link not found : " + "Failed")
            except:
                upgrade = "//button[contains(text(),'UPGRADE NOW')]"
                element19 = WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, upgrade)))
                upgrade_dis = driver.find_element_by_xpath(upgrade).is_displayed()
                if (upgrade_dis == True):
                    element16 = driver.find_element_by_xpath(upgrade).click()
                if (donot_sell == True):
                    print("Do Not Sell My Info in Checkout Displayed : " + "Passed")
                else:
                    print("Do Not Sell My Info in Checkout link not found : " + "Failed")
            time.sleep(5)

    # Step 7 : Check - sitemap.xml
    site = "sitemap.xml"
    Append = URL + "/" + site
    driver.get(Append)
    urlset = "//*[@class='html-attribute-value']"
    element15 = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.XPATH, urlset)))
    urlsetp = driver.find_element_by_xpath("//*[@class='html-attribute-value']").is_displayed()
    if (urlsetp == True):
        print("sitemap Displayed : " + "Passed")
    else:
        print("sitemap not found : " + "Failed")
    time.sleep(5)

    # Step 8 : Check - Robots.txt
    txt = "robots.txt"
    Append2 = URL + "/" + txt
    driver.get(Append2)
    pre_gb = "//pre[contains(text(),'Googlebot')]"
    element15 = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.XPATH, pre_gb)))
    urlsetr = driver.find_element_by_xpath(pre_gb).is_displayed()
    if (urlsetr == True):
        print("robots Displayed : " + "Passed")
    else:
        print("robots not found : " + "Failed")

for a in x:
    # print(a)
    print(" ")

# def get_url(env, brand, campaign):
#     query = "select * from campaign_urls where brand = " + brand + "and campaign = " + campaign

# # Step 1 : Check - Terms & Conditions
# # Store all locators in content_locators table
# # Replicate get_element_locator function from CommonUtilities.java file
# element = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Terms & Conditions')]")))
# TC = driver.find_element_by_xpath("//a[contains(text(),'Terms & Conditions')]")
#
# TC.click()
# TC1 = "//h1[contains(text(),'Terms of Use and Conditions of Purchase')]"
# element = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, TC1)))
# element1 = driver.find_element_by_xpath("//div[@id='popupcontent']").text
# element2 = element1.rstrip()
# File2 = open("F:\Python\GR\Content\Terms of Use and Conditions\Purchase.txt", "r")
# File1 = (File2.read())
# File1.rstrip()
#
# if (element2 == File1):
#     print("Terms of Use and Conditions of Purchase : " + "Passed")
# else:
#     print("Terms of Use and Conditions of Purchase : " + "Failed")
#
# # Step 2 : Check - Sales Tax link
#
# element3 = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Sales Tax')]")))
# TC4 = driver.find_element_by_xpath("//a[contains(text(),'Sales Tax')]")
# TC4.click()
#
# try:
#     element9 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'Sales Tax')]")))
#     print("Sales Tax : " + "Passed")
# except NoSuchElementException:
#     print("Sales Tax link not found : " + "Failed")
#
# time.sleep(5)
#
# # Step 3 : Check - Privacy Policy
# element = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Privacy Policy')]")))
# TC3 = driver.find_element_by_xpath("//a[contains(text(),'Privacy Policy')]")
# TC3.click()
#
# p = driver.current_window_handle
# chwd = driver.window_handles
# for w in chwd:
#     # switch focus to child window
#     if (w != p):
#         driver.switch_to.window(w)
#         break
#         time.sleep(0.9)
#         print("Child window title: " + driver.title)
#
# TC1 = "//h1[contains(text(),'Privacy Policy')]"
# element = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, TC1)))
# element4 = driver.find_element_by_xpath("//div[@id='content']").text
# element5 = element4.rstrip()
# File3 = open("F:\Python\GR\Content\Terms of Use and Conditions\Privacy.txt", "r")
# File4 = (File3.read())
# File5 = File4.rstrip()
# if (element5 == File5):
#     print("Privacy Policy : " + "Passed")
# else:
#     print("Privacy Policy : " + "Failed")
# time.sleep(5)
# element6 = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Your California Privacy Rights')]")))
# TC4 = driver.find_element_by_xpath("//a[contains(text(),'Your California Privacy Rights')]")
# TC4.click()
#
# try:
#     element9 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//h3[@id='Your_California_Privacy_Rights']")))
#     print("Your California Privacy Rights : " + "Passed")
# except NoSuchElementException:
#     print("Your California Privacy Rights link not found : " + "Failed")
#
# # Step 4 : Check - live chat & Phone number
#
# element = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Customer Service')]")))
# TC4 = driver.find_element_by_xpath("//a[contains(text(),'Customer Service')]")
# TC4.click()
#
# driver.switch_to.window(driver.window_handles[2])
#
# element = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Click here to reach us via live chat')]")))
# TC8 = driver.find_element_by_xpath("//span[contains(text(),'Click here to reach us via live chat')]")
# TC8.click()
# Number = driver.find_element_by_xpath("//*[@id='main']/div/div/div[4]/div[1]/div/p/a").is_displayed()
# if (Number == True):
#     print("Number Displayed : " + "Passed")
# else:
#     print("Number not found : " + "Failed")
# chat = driver.find_element_by_xpath("//span[contains(text(),'Click here to reach us via live chat')]").is_displayed()
# if (chat == True):
#     print("live chat : " + "Passed")
# else:
#     print("live chat link not found : " + "Failed")
#
# # Step 5 : Check - Do not sell my info link
# driver.switch_to.window(driver.window_handles[2])
# # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# driver.get(URL)
# element = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, "//a[@id='donot-sell']")))
# Number = driver.find_element_by_xpath("//a[@id='donot-sell']").is_displayed()
# if (Number == True):
#     print("Do Not Sell My Info in Home page Displayed : " + "Passed")
# else:
#     print("Do Not Sell My Info in Home page link not found : " + "Failed")
# element6 = driver.find_element_by_xpath("(//a[@class='cta'])[1]").click()
# if (Number == True):
#     print("Do Not Sell My Info in SAS Displayed : " + "Passed")
# else:
#     print("Do Not Sell My Info in SAS link not found : " + "Failed")
# try:
#     kit_id = "//div[@data-productid='CSPG029']//div[@class='sas-checkbox clearfix']//h3"
#     element13 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, kit_id)))
#     element12 = driver.find_element_by_xpath(
#         kit_id).click()
#     # element13 = WebDriverWait(driver, 100).until(
#     #    EC.visibility_of_element_located((By.XPATH, "//div[@data-giftproduct='CS2A0686']//div[@class='sas-checkbox clearfix']//a")))
#     # element12 = driver.find_element_by_xpath("//div[@data-giftproduct='CS2A0686']//div[@class='sas-checkbox clearfix']//a").click()
#
#     element9 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//a[@class='cta']")))
#     element10 = driver.find_element_by_xpath("//a[@class='cta']").click()
# except NoSuchElementException:
#     element11 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//button[@class='button checkout']")))
#     element12 = driver.find_element_by_xpath("//button[@class='button checkout']").click()
# if (Number == True):
#     print("Do Not Sell My Info in Checkout Displayed : " + "Passed")
# else:
#     print("Do Not Sell My Info in Checkout link not found : " + "Failed")
#
# # Step 6 : Check - T&C Popup link functionality on checkout page
# TC_PU = "//*[@id='tncEntryKit']/p/span[1]/a"
# try:
#     element9 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//*[@id='tncEntryKit']/p/span[1]/a")))
#     element10 = driver.find_element_by_xpath("//*[@id='tncEntryKit']/p/span[1]/a").click()
#
#     element13 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//*[@id='popupRevealModal']/div[2]/button")))
#     TC_PU_Cs = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").is_displayed()
#     element14 = driver.find_element_by_xpath("//*[@id='popupRevealModal']/div[2]/button").click()
# except NoSuchElementException:
#     element11 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//button[@class='button checkout']")))
#     element12 = driver.find_element_by_xpath("//button[@class='button checkout']").click()
# if (TC_PU_Cs == True):
#     print("T&C Popup link in Checkout Displayed : " + "Passed")
# else:
#     print("T&C Popup link in Checkout link not found : " + "Failed")
#
# # Step 6 : Check - Presence of AccessiBe tool on checkout page
# P_ABE = "//div[@aria-label='Open the Accessibility Interface (Can also be opened using the Alt+9 Key)']"
#
# try:
#     element9 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH,
#                                           "//div[@aria-label='Open the Accessibility Interface (Can also be opened using the Alt+9 Key)']")))
#     element10 = driver.find_element_by_xpath(
#         "//div[@aria-label='Open the Accessibility Interface (Can also be opened using the Alt+9 Key)']").click()
#
#     element13 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//*[@aria-label='Close Accessibility Interface']")))
#     TC_PU_Cs = driver.find_element_by_xpath("//*[@aria-label='Close Accessibility Interface']").is_displayed()
#     element14 = driver.find_element_by_xpath("//*[@aria-label='Close Accessibility Interface']").click()
# except NoSuchElementException:
#     element11 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//button[@class='button checkout']")))
#     element12 = driver.find_element_by_xpath("//button[@class='button checkout']").click()
# if (TC_PU_Cs == True):
#     print("Presence of AccessiBe tool link in Checkout Displayed : " + "Passed")
# else:
#     print("Presence of AccessiBe tool link in Checkout link not found : " + "Failed")
#
# # Step 7 : Check - sitemap.xml
# site = "sitemap.xml"
# Append = URL + "/" + site
# driver.get(Append)
# urlset = "//*[@class='html-attribute-value']"
# element15 = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, urlset)))
# urlsetp = driver.find_element_by_xpath("//*[@class='html-attribute-value']").is_displayed()
# if (urlsetp == True):
#     print("sitemap Displayed : " + "Passed")
# else:
#     print("sitemap not found : " + "Failed")
#
# # Step 8 : Check - Robots.txt
# txt = "robots.txt"
# Append2 = URL + "/" + txt
# driver.get(Append2)
# pre_gb = "//pre[contains(text(),'Googlebot')]"
# element15 = WebDriverWait(driver, 100).until(
#     EC.visibility_of_element_located((By.XPATH, pre_gb)))
# urlsetr = driver.find_element_by_xpath(pre_gb).is_displayed()
# if (urlsetr == True):
#     print("robots Displayed : " + "Passed")
# else:
#     print("robots not found : " + "Failed")
#
# driver.close()
driver.quit()


#
#

def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
