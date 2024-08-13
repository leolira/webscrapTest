import requests
from bs4 import BeautifulSoup

url = 'https://blogbbm.com/manga/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

manga_titles = []

lines = soup.find_all('tr')

links=[]

def get_links(lines):
    for line in lines:
        links.extend(line.find_all('a', href=lambda href: href.startswith('https://blogbbm.com/manga/')))
    return(links)

links = get_links(lines)

def get_manga_titles(links):
    for link in links:
        manga_titles.append(link.text)
    return(manga_titles)

manga_titles = get_manga_titles(links)

for t in manga_titles:
    print (t)