import requests
 
url = "https://www.sejuku.net/blog/"
 
response = requests.get(url)
response.encoding = response.apparent_encoding
 
print(response.text)