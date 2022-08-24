import requests
from bs4 import BeautifulSoup
headers = {
    "User-agent": "Chrome/100.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

url = "https://www.google.com/search?q=sleep+and+beyond"
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'lxml')
link = soup.find_all("div", class_="yuRUbf")

for urlLink in link:
    detail =urlLink.find("a")
    url= detail["href"]
    print(url)
