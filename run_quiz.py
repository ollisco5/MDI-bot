from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from get_data import get_data
from url import GUI
from login import login




def dummy_run_quiz(url, submit=False):
    driver = login(url)
    driver.delete_all_cookies()
    
    # Press Begin
    driver.switch_to.frame(1)
    

    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(len(buttons))
    print(buttons[-1].text)
    buttons[-1].click()
    
    time.sleep(5)
    
    driver.switch_to.frame(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fNHEA_cSXm"))
    )
    
    elements = driver.find_elements(By.CLASS_NAME, "fNHEA_cSXm")

    for i in elements:
        i.click()

    if submit:
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        buttons[-1].click()
        
        comfirm_buttons = driver.find_elements(By.TAG_NAME, 'button')
        comfirm_buttons[-1].click()

    time.sleep(2)
    driver.quit()

  

def delete_wrong_answers(url, data):
    driver = login(url)
    # Press latest attempt
    time.sleep(4)

    driver.switch_to.frame(1)
    buttons = driver.find_elements(By.CLASS_NAME, 'fbyHH_vIby')
    buttons[-1].click()

    time.sleep(2)
    

    # cQHeE_cSuF
    elements = driver.find_elements(By.CLASS_NAME, "cQHeE_cSuF")

    d = {}
    for e in elements:
        txt = e.text
        rows = txt.split("\n")
        question = rows[0]
        answers = rows[1:]
        
        
        
        if "Incorrect answer:" in txt:
            test_list = []
            for i in range(len(answers)):
                if answers[i] == ', Not Selected':
                    test_list.append(answers[i - 1])

            d[question] = test_list
        elif "Correct answer:" in txt:
            d[question] = [rows[rows.index("Correct answer:") + 1]] # Select row after correct answear

        else:
            print("NO ANSWEAR CHOSEN")
        
    return d


if __name__ == "__main__":
    print("Starting Program")
    url = GUI

    print("-"*100)
    data = delete_wrong_answers(url, {})
    for k,v in data.items():
        print(f"({len(v)}) {k}: {v}") 