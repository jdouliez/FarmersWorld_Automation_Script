#!/usr/bin/env python3

from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import os
from datetime import datetime
from config import *

now = datetime.now()

def pprint(text):
    print("[" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] " + text)


try:
    pprint("[+] Killing all previous browsers instances")
    os.system("killall firefox-esr > /dev/null 2>&1")

    pprint("[+] Launching browser")
    options=Options()
    #options.set_preference('profile', FIREFOX_PROFILE_LOCATION)
    profile = webdriver.FirefoxProfile(FIREFOX_PROFILE_LOCATION)
    options.profile = profile
    options.headless = HEADLESS_MODE
    driver = webdriver.Firefox(options=options)

    pprint("[+] Getting https://farmerscript.online/")
    driver.get("https://farmerscript.online/") 
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div/main/div/div/div/h1"), 'Please log in first'))

    pprint("[+] Logging in")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/main/header/div/div/div[2]/div/button").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div/main/header/div/div/div[2]/div[2]/button"), 'swvmm.c.wam'))

    pprint("[+] Checking that the site is running by reading info")
    fee_text = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div/h3").text
    print(f"   --> {fee_text}")

    pprint(f"[+] Waiting {BROWSER_OPENED_DELAY} minutes with browser opened")
    time.sleep(60 * BROWSER_OPENED_DELAY)

    pprint("[+] Closing browser")
    driver.close()

    pprint("[+] Cleaning traces")
    os.system("rm -rf /tmp/tmp*")

except Exception as ex:
    pprint(f"[-] Sending error email")
    SUBJECT = "Erreur lors de l'exécution du script FarmersWorld"
    BODY = "STACKTRACE : \n" + str(ex)
    os.system(f"echo \"Subject: {SUBJECT}\n\n{BODY}\" | msmtp \"{EMAIL_TO}\"")

print(f"")
