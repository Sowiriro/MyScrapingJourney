import requests
 
url = "https://product.starbucks.co.jp/goods/tumbler/4524785332171/?category=goods%2Ftumbler"
 
response = requests.get(url)

 
print(response)