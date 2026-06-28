import requests
import smtplib
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
  }

USER_EMAIL = os.environ.get("USER_EMAIL")
PASSWORD = os.environ.get("APP_PASSWORD")
TO_ADDRS = os.environ.get("TO_EMAIL")
smtp = smtplib.SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login(user=USER_EMAIL, password=PASSWORD)
github_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(github_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
dollar_price = soup.find(name="span", class_="a-price-whole")
cent_price = soup.find(name="span", class_="a-price-fraction")
pot_price = f"{dollar_price.text}{cent_price.text}"
pot_price = float(pot_price)



print(pot_price)
if pot_price < 100:
    print("sending email")
    smtp.sendmail(from_addr=USER_EMAIL, to_addrs=TO_ADDRS, msg=f"Subject: Amazon Price Alert\n\nYour favorite instant cooker pot just hit the LOWEST PRICE of ${pot_price}")
    print("email sent")