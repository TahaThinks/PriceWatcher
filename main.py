import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(url=product_url)
print(response.text)

