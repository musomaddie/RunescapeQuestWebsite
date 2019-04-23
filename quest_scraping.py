import requests
from bs4 import BeautifulSoup


def testing(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    h1 = soup.find('h1')
    print(h1.text)


def test_all():
    urls = ['https://runescape.wiki/w/The_Blood_Pact',
            'https://runescape.wiki/w/Cold_War',
            'https://runescape.wiki/w/The_Chosen_Commander',
            'https://runescape.wiki/w/The_World_Wakes']
    for u in urls:
        testing(u)


testing('https://runescape.wiki/w/Cold_War')
test_all()
