import requests

from bs4 import BeautifulSoup


URL = "https://www.kinopoisk.ru/"
GET_FILM = ""

content = requests.get(URL).content

soup = BeautifulSoup(content, 'lxml')

for child in soup.recursiveChildGenerator():
    if child.name == "h3":
        print(child.text)
