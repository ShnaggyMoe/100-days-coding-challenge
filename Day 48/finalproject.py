from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(5)

langauge_button = driver.find_element(By.CSS_SELECTOR, value=".langSelectButton.title")
langauge_button.click()
cookie_products = driver.find_elements(By.CLASS_NAME, value="product")
total_cookies = driver.find_element(By.ID, value="cookies")
total_cookies_2 = total_cookies.text
total_cookies_2 = total_cookies_2.split(" ")
all_cookies = int(total_cookies_2[0])



upgrade_list = []
seconds = time.time()
five_secs = time.time() + 5
cookie_timer = True
while cookie_timer:
    big_cookie_button = driver.find_element(By.ID, value="bigCookie")
    big_cookie_button.click()
    if five_secs - time.time() < 0:
        upgrade_list = []
        all_cookies = int(total_cookies.text.split(" ")[0])
        for product in cookie_products:
            if len(product.text.split("\n")) > 1:
                split_product = product.text.split("\n")
                shop_product = split_product[1].replace(",", "")
                store_upgrades = int(shop_product)
                if all_cookies - store_upgrades >= 0:
                    upgrade_list.append(shop_product)
        expensive_item = max(upgrade_list)
        for product in cookie_products:
            price = product.text
            if len(product.text.split("\n")) > 1:
                new_variable = price.split("\n")
                if new_variable[1] == expensive_item:
                    product.click()
        five_secs = time.time() + 5
    if time.time() - seconds > 15:
        cookie_timer = False
cps = driver.find_element(By.ID, value="cookiesPerSecond")
print(cps.text)