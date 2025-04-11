import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib
import config

load_dotenv()

MY_EMAIL = os.getenv('EMAIL_ADDRESS')
MY_PASSWORD = os.getenv('EMAIL_PASSWORD')

header = config.headers

url = "https://www.amazon.com.br/Protetor-Solar-Facial-Oleosa-NEUTROGENA/dp/B08NVMP2YZ?th=1"
PRICE = 50


response = requests.get(url, headers=header)

web = response.text

soup = BeautifulSoup(web, "html.parser")
price = soup.select_one('span.a-price-whole')
price_float = float(price.getText().strip().replace(',', '.'))
print(price_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)
if price_float < PRICE:
    message = f"{title} is on sale for {price_float}"
    message = message.encode('utf-8')
    connection = smtplib.SMTP(os.getenv("SMTP"), port=int(os.getenv("PORT")))
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url} "
    )
else:
    print("ta caro")
