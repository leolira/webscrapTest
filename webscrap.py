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
        links.extend(line.find_all('a', href=lambda href: href and href.startswith('https://blogbbm.com/manga/')))
    return(links)

links = get_links(lines)

for link in links:
    print(link.text)