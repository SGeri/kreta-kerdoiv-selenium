from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser = Service("chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

'''
first button /html/body/root/normal-survey-flow/normal-survey-start-container/survey-start/survey-start-footer/footer/section[2]/footer-start-button/button
q1: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[3]/input
q2: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[4]/input
next: /html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]
q3: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[5]/input
q4: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[1]/input
next: /html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]
q5: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[5]/input
q6: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[2]/input
next: /html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]
q7: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input
q8: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[5]/label
next: /html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]
q9: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input
q10: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[1]/input
next: /html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]
q11: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/label
text: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/multi-line-accessor/textarea
next: /html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]
finish: /html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div[2]/button
'''

textarea_input = "asdasd"

total = 0

for i in range(10):
    try: 
        driver.get("https://szuloikerdoiv44623.unipoll.hu/PagesForResponse/normalsurvey/response?surveyid=20000150")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-start-container/survey-start/survey-start-footer/footer/section[2]/footer-start-button/button')))

        start_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-start-container/survey-start/survey-start-footer/footer/section[2]/footer-start-button/button')
        start_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[3]/input')))
        q1 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[3]/input')
        q1.click()

        q2 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[4]/input')
        q2.click()

        next_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]')
        next_button.click()

        time.sleep(0.6)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[5]/input')))
        q3 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[5]/input')
        q3.click()

        q4 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[3]/input')
        q4.click()

        next_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]')
        next_button.click()

        time.sleep(0.6)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')))
        q5 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')
        q5.click()

        q6 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[1]/input')
        q6.click()

        next_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]')
        next_button.click()

        time.sleep(0.6)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')))
        q7 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')
        q7.click()

        q8 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[1]/input')
        q8.click()

        next_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]')
        next_button.click()

        time.sleep(0.6)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')))
        q9 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')
        q9.click()

        q10 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/single-select-accessor/div[1]/input')
        q10.click()

        next_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]')
        next_button.click()

        time.sleep(0.6)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')))
        q11 = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[1]/div/form/single-select-accessor/div[1]/input')
        q11.click()

        text_area = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div/app-question-frame[2]/div/form/multi-line-accessor/textarea')
        text_area.send_keys(textarea_input)

        next_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/normal-survey-footer/footer/section[3]/footer-paginator/div/button[2]')
        next_button.click()

        time.sleep(0.6)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div[2]/button')))
        finish_button = driver.find_element(By.XPATH, '/html/body/root/normal-survey-flow/normal-survey-container/survey/div/div/div/div[2]/button')
        finish_button.click()

        time.sleep(0.8)

        popup_finish = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/app-dialog/div/div[2]/div/button[2]')
        popup_finish.click()

        total += 1
        print("total:", total)

    except KeyboardInterrupt:
        break

    except Exception as e:
        print('error:', e)
        continue

time.sleep(30)