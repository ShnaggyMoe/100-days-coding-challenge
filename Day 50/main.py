from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random

load_dotenv()

TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/sllEzJ_CX5Ht7rfEBxKYU7h-xJi0X8EK"
facebark_id = os.environ.get("FACEBARK_ID")
facebark_password = os.environ.get("FACEBARK_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(TINDOG_URL)

def login():
    login_button = driver.find_element(By.CLASS_NAME, value="btn-tindog-login")
    login_button.click()
    login_with_facebark = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-facebark.tindog-login-method")))
    login_with_facebark.click()
    driver.switch_to.window(driver.window_handles[-1])
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys(facebark_id)
    password_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "pass")))
    password_field.send_keys(facebark_password)
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()
    driver.switch_to.window(driver.window_handles[0])

def dismiss_popups():
    allow_location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    allow_location.click()
    notifications = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    notifications.click()
    cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    cookies.click()

def swipe():
    while True:
        nope_buttons = driver.find_elements(By.CLASS_NAME, "btn-nope")
        if len(nope_buttons) == 0:
            break
        else:
            like_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-like")))
            buttons = [nope_buttons[0], like_button]
            chosen_button = random.choice(buttons)
            driver.execute_script("arguments[0].click();", chosen_button)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-nope")))

login()
dismiss_popups()
swipe()