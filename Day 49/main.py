from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Loading in credentials
load_dotenv()

ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

#Selenium setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

#Filling in info
login_button = driver.find_element(By.ID, value="login-button")
login_button.click()
email_input = driver.find_element(By.ID, value="email-input")
password_input = driver.find_element(By.ID, value="password-input")
email_input.send_keys(ACCOUNT_EMAIL)
password_input.send_keys(ACCOUNT_PASSWORD)
submit_button = driver.find_element(By.ID, value="submit-button")
submit_button.click()

#Verifying that program is in the correct webpage
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "type-filter"))
)

time_list = driver.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")
for time in time_list:
    time_text = time.text
    time_text_2 = time_text.split(": ")
    if time_text_2[1] == "6:00 PM":
        day_group = time.find_element(By.XPATH, "ancestor::div[4]")
        class_card = time.find_element(By.XPATH, "ancestor::div[3]")
        print(class_card.get_attribute("id"))
        day_group_id = day_group.get_attribute("id")
        if "tue" in day_group_id:
            booked = class_card.get_attribute("data-user-booked")
            waitlisted = class_card.get_attribute("data-user-waitlisted")
            class_detail = class_card.find_element(By.CSS_SELECTOR, value="h3[id^='class-name']")
            class_detail_text = class_detail.text
            if booked == "true":
                print("✓ Already booked: Spin Class on Tue, Aug 12")
                pass
            elif waitlisted == "true":
                print("✓ Already on waitlist: HIIT Class on Tue, Aug 12")
                pass
            else:
                join_waitlist_button = class_card.find_element(By.CSS_SELECTOR, "button[id^='book-button']")
                join_waitlist_button.click()
                class_name = class_card.find_element(By.CSS_SELECTOR, "h3[id^='class-name']").text
                day_group_list = day_group_id.split("-")
                day_group_list[3] = day_group_list[3].replace("(", "")
                day_group_list[4] = day_group_list[4].replace(")", "")
                day_group_list[5] = day_group_list[5].replace(")", "")
                today = f"{day_group_list[3]} {day_group_list[4]} {day_group_list[5]}"
                print(f"✔️ Booked: {class_name} on {today}")