from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from env import USERNAME, PASSWORD
from login import login
from url import GUI

def get_data(url):
    driver = login(url)
    
    time.sleep(1)
    driver.switch_to.frame(1)

    time.sleep(1)

    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(len(buttons))
    print(buttons[-1].text)
    buttons[-1].click()
    
    time.sleep(2)

    driver.switch_to.frame(1)

    time.sleep(2)
    
    elements = driver.find_elements(By.CLASS_NAME, "gmVuP_gasz")

    d = {}
    for e in elements:
        el = e.text.split("\n")
        d[el[0]] = el[1:]

    driver.quit()
    return d


if __name__ == "__main__":
    data = get_data(GUI)
    for k,v in data.items():
        print(f"{k}: {v} ({len(v)})")