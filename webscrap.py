import requests
from bs4 import BeautifulSoup

url = 'https://blogbbm.com/manga/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

manga_titles = []

cells = soup.find_all('td')

def mangaSearch(cells):
    for cell in cells:
        links = cell.find_all('a', href=lambda href: href and href.startswith('https://blogbbm.com/manga/'))
        manga_titles.append(links)
        print(manga_titles)
    return manga_titles

print(manga_titles)

for manga in manga_titles:
    print(manga.text)
