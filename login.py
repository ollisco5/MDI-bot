from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from env import USERNAME, PASSWORD

def login(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.delete_all_cookies()
    driver.get(url)

    user_name = driver.find_element(By.ID, "userNameInput")

    user_name.send_keys(USERNAME)
    user_name.send_keys(Keys.RETURN)

    password = driver.find_element(By.ID, "passwordInput")

    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)

    return driver