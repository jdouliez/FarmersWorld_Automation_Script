#!/usr/bin/env python3

from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import os
from datetime import datetime

#### Configuration ####
FIREFOX_PROFILE_LOCATION = '/root/.mozilla/firefox/fshj8qps.default-esr'  ### CHANGE THIS
BROWSER_OPENED_DELAY = 3
#######################

now = datetime.now()

def pprint(text):
    print("[" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] " + text)


pprint("[+] Killing all previous browsers instances")
os.system("killall firefox-esr > /dev/null 2>&1")


pprint(f"[+] Launching browser")
options=Options()
#options.set_preference('profile', FIREFOX_PROFILE_LOCATION)
profile = webdriver.FirefoxProfile(FIREFOX_PROFILE_LOCATION)
options.profile = profile
options.headless = True
driver = webdriver.Firefox(options=options)


pprint(f"[+] Getting https://farmerscript.online/")
driver.get("https://farmerscript.online/") 
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div/main/div/div/div/h1"), 'Please log in first'))


pprint(f"[+] Logging in")
driver.find_element(By.XPATH, "/html/body/div[1]/div/main/header/div/div/div[2]/div/button").click()
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div/main/header/div/div/div[2]/div[2]/button"), 'swvmm.c.wam'))


pprint(f"[+] Checking that site is running by reading info")
energy_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/header/div/div/div[2]/div[1]/span").text
print(f"   --> Energy level : {energy_text}")


pprint(f"[+] Waiting {BROWSER_OPENED_DELAY} minutes with browser opened")
time.sleep(60 * BROWSER_OPENED_DELAY)

pprint(f"[+] Closing browser")
driver.close()

pprint(f"[+] Cleaning traces")
os.system("rm -rf /tmp/tmp*")

print(f"")