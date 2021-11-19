import requests
from bs4 import BeautifulSoup

url  = "https://www.amazon.co.uk/Apple-AirPods-MagSafe-charging-case/dp/B09JQZ5DYM/ref=sr_1_1_sspa?crid=28JKWHVNQVGTL&keywords=airpods+pro&qid=1637237892&sprefix=air%2Caps%2C174&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTkZUSVVaTVFKNE5TJmVuY3J5cHRlZElkPUEwMjYyMDEwMTVSNThSTTZTREFKMiZlbmNyeXB0ZWRBZElkPUEwOTExMzUzSzhHOVdJUEFDRlFEJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

HEADERS =({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
page = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(page.content)

price = soup.find_all(class_='a-price a-text-price a-size-medium apexPriceToPay')

print(price)
