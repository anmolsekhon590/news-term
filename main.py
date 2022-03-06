import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.cbc.ca/news")
content = BeautifulSoup(response.content, "html.parser")

node = content.findAll(("h3", {"class": "headline"}))
for i in range(10):
    print(i+1, node[i+1].text)
