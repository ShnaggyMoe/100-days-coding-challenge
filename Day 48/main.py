from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

unordered_list_event = driver.find_element(By.CSS_SELECTOR, value=".medium-widget.event-widget.last")
event_list_items = unordered_list_event.find_elements(By.TAG_NAME, value="li")
name_list = []
time_list = []

for item in event_list_items:
    name_item = item.find_element(By.TAG_NAME, value="a")
    time_item = item.find_element(By.TAG_NAME, value="time")
    name_list.append(name_item.text)
    time_list.append(time_item.text)

new_dict = {}
for index, value in enumerate(time_list):
    new_dict[index] = {"time": value, "name": name_list[index]}

print(new_dict)



# driver.close()
driver.quit()