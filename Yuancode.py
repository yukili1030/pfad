import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.hko.gov.hk/en/tide/ttext.htm")
html = response.text
soup = BeautifulSoup(html,"html.parser")
all_titles = soup.findAll("td")
for title in all_titles:
    print(title)
