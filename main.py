from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from env import USERNAME, PASSWORD


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://canvas.kth.se/courses/31508/quizzes")

    user_name = driver.find_element_by_id("userNameInput")

    user_name.send_keys(USERNAME)
    user_name.send_keys(Keys.RETURN)

    password = driver.find_element_by_id("passwordInput")

    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)

    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
    PATH = "C:\Program Files (x86)\Chromedriver\chromedriver.exe"
    main()
