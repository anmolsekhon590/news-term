import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.cbc.ca/news")
content = BeautifulSoup(response.content, "html.parser")

for node in content.findAll(("h3", {"class": "headline"})):
    print(node.text)
