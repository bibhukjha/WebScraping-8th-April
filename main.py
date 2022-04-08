from bs4 import BeautifulSoup
import requests

link = "https://www.google.com/doodles"

page = requests.get(link)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)
