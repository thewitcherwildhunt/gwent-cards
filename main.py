from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://www.playgwent.com/ru/decks/')
html = response.read().decode()
soup = BeautifulSoup(html)
for link in soup.find_all('a'):
    print(link)