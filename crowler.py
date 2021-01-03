import requests
from bs4 import BeautifulSoup
 
url = "https://product.starbucks.co.jp/goods/tumbler/4524785332171/?category=goods%2Ftumbler"
 
response = requests.get(url)

soup = BeautifulSoup(response.content,  'html.parser')

elems = soup.find_all("p", class_="notification")
for e in elems:
    print(e.getText())

print(response.url)