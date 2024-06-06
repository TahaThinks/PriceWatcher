import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(url=product_url)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)
price_digit = soup.find(name="span", class_="a-price-whole").text
price_decimal = soup.find(name="span", class_="a-price-fraction").text

price = float(f"{price_digit}{price_decimal}")
print(price)