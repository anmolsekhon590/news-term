import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.cbc.ca/news")
content = BeautifulSoup(response.content, "html.parser")

counter = 0
for node in content.findAll(("h3", {"class": "headline"})):
    if counter > 10:
        break
    print("- ", node.text)

    counter = counter + 1
