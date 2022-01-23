from webbrowser import Chrome
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *
import time
from url import *
from login import login


def dummy_run_quiz(driver, url, submit=False):
    #driver = login(url)    
    # Press Begin
    driver.get(url)

    driver.switch_to.frame(1)

    time.sleep(6)
    
    buttons = driver.find_elements(By.TAG_NAME, "button")
    buttons[-1].click()
    
    time.sleep(5)
    
    driver.switch_to.frame(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fNHEA_cSXm"))
    )

    d = get_data(driver)
    
    elements = driver.find_elements(By.CLASS_NAME, "fNHEA_cSXm")

    for i in elements:
        i.click()

    if submit:
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        buttons[-1].click()
        
        comfirm_buttons = driver.find_elements(By.TAG_NAME, 'button')
        comfirm_buttons[-1].click()

    time.sleep(6)
    return d



def get_data(driver):
    elements = driver.find_elements(By.CLASS_NAME, "gmVuP_gasz")

    d = {}
    for e in elements:
        el = e.text.split("\n")
        d[el[0].strip() + el[1].strip()] = list(map(lambda x: x.strip(), el[1:]))

    return d

def smart_run_quiz(driver, url, data: dict):
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    time.sleep(6)

    driver.switch_to.frame(1)

    buttons = driver.find_elements(By.TAG_NAME, "button")
    buttons[-1].click()

    time.sleep(6)

    driver.switch_to.frame(1)

    time.sleep(10)

    current_data = get_data(driver)

    for k,v in current_data.items():
        print(f"({len(v)}) {k}: {v}") 
    print("-"*20)
    for k,v in data.items():
        print(f"({len(v)}) {k}: {v}") 

    time.sleep(5)

    answer_buttons = driver.find_elements(By.CLASS_NAME, "fNHEA_cSXm")
    print(len(answer_buttons))


    for k, v in data.items():
        print(list(current_data.keys()), k)
        base_index = list(current_data.keys()).index(k) * 3
        all_answers = current_data[k]
        chosen_answer_index = all_answers.index(v[0].strip())
        print(f"Q: {k} A: {v[0]} I: {base_index + chosen_answer_index}")
        answer_buttons[base_index + chosen_answer_index].click()


    submit = True
    if submit:

        buttons = driver.find_elements(By.TAG_NAME, 'button')
        buttons[-1].click()
        
        comfirm_buttons = driver.find_elements(By.TAG_NAME, 'button')
        comfirm_buttons[-1].click()

    time.sleep(5)
  

def delete_wrong_answers(driver, url, data):
    # driver = login(url)
    # Press latest attempt
    driver.get(url)
    time.sleep(6)

    driver.switch_to.frame(1)
    buttons = driver.find_elements(By.CLASS_NAME, 'fbyHH_vIby')
    buttons[-1].click()

    time.sleep(6)

    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "alertHolder"))
    )
    
    # cQHeE_cSuF
    elements = driver.find_elements(By.CLASS_NAME, "cQHeE_cSuF")

    for e in elements:
        txt = e.text
        rows = txt.split("\n")
        question = rows[0].strip()




        for row in rows:
            if row.strip() not in ["Correct answer:", "Incorrect answer:", ", Not Selected"]:
                tmp = question + row.strip()
                if tmp in list(data.keys()):
                    question = tmp
                    break
        
        for i, v in enumerate(rows):
            v = v.strip()
            if v == "Correct answer:":
                data[question] = [rows[i+1]]

            elif v == "Incorrect answer:":
                try:
                    print(rows[i + 1], "Incorrect")
                    data[question].remove(rows[i+1])

                except Exception as e:
                    print(e, data[question], rows[i+1])


    for k,v in data.items():
        print(f"({len(v)}) {k}: {v}") 

    return data


if __name__ == "__main__":
    url = PROTOTYPING
    print("Starting Program")
    driver = login(url)
    should_exit = True
    
    print("Dummy run")
    data = dummy_run_quiz(driver, url, False)

    data = delete_wrong_answers(driver, url, data)

    print("Check 1")
    for k, v in data.items():
        if len(v) != 1:
            should_exit = False

    if should_exit:
        quit()

    print("Smart run 1")
    smart_run_quiz(driver, url, data)

    data = delete_wrong_answers(driver, url, data)

    print("Check 2")
    for k, v in data.items():
        if len(v) != 1:
            should_exit = False

    if should_exit:
        quit()


    print("Final smart run")
    smart_run_quiz(driver, url, data)

    driver.quit()