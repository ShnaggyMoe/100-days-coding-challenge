from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# # articles.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver = webdriver.Chrome()
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
first_name_button = driver.find_element(By.CSS_SELECTOR, value=".form-control.top")
last_name_button = driver.find_element(By.CSS_SELECTOR, value=".form-control.middle")
email_address_button = driver.find_element(By.CSS_SELECTOR, value=".form-control.bottom")
first_name_button.send_keys("Anakin")
last_name_button.send_keys("Skywalker")
email_address_button.send_keys("AnakinSkywalker@gmail.com")
sign_up_button = driver.find_element(By.CSS_SELECTOR, value=".btn.btn-lg.btn-primary.btn-block")
sign_up_button.click()