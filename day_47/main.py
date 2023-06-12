import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url ="https://www.amazon.com/lzteck-Insulated-Lunch-Bag-Dishwasher/dp/B09Z6LD4K1/ref=sr_1_11_sspa?crid=" \
     "3CVQAVVG7WPP3&keywords=pots+and+pans+with+flat+lids+removable+handles&qid=1686497753&sprefix=pots+" \
     "and+pans+with+flat+lids+removable+handles%2Caps%2C155&sr=8-11-spons&ufe=app_do%3Aamzn1.fos.18630bbb-" \
     "fcbb-42f8-9767-857e17e03685&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMzIwUzFHUlBFWlo5JmVuY3J5cHRlZEl" \
     "kPUEwMjI5NzY2MUFXQ1BERUc1SllZRiZlbmNyeXB0ZWRBZElkPUEwNDIzNjY5MlpZM1lPRzBPNlJBTiZ3aWRnZXROYW1lPXNwX" \
     "210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
price_float = float(price)
print(price_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 140
YOUR_EMAIL = ""
YOUR_PASSWORD = ""

if price_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )

