import requests
from bs4 import BeautifulSoup


def get_quest_name(soup):
    return soup.find('h1').text


def find_quest_details(soup):
    for t in soup.find_all('table'):
        if "questdetails" in t['class']:
            return t
    return None


def find_quest_infobox(soup):
    for t in soup.find_all('table'):
        if 'id' not in t.attrs:
            continue
        if t['id'] == "infobox-quest":
            return t


def find_is_free(quest_details):
    for t in quest_details.find_all('tr'):
        try:
            if t.find('th').text == "Member requirement":
                return t.find('td').text == " Free to play"
        except AttributeError:
            continue


def find_requirements(quest_details):
    for tr in quest_details.find_all('tr'):
        try:
            if tr.find('th').text.strip() == "Requirements":
                return tr.find('td')
        except AttributeError:
            continue


def find_quests(requirements):
    quests = None
    quests_found = False
    for tr in requirements.find_all('tr'):
        try:
            if quests_found:
                quests = tr.find('td')
            if tr.find('th').text.strip() == "Quests:":
                quests_found = True
        except AttributeError:
            continue
    if quests is None:
        return []
    # let's just find this quest
    this_quest = next(quests.children).find('ul')
    quests = []
    for child in this_quest:
        quests.append(child.contents[0].text)
    return quests


def find_difficulty_or_length(quest_details, opt):
    for t in quest_details.find_all('tr'):
        try:
            if t.find('th').text == "Official {}".format(opt):
                return t.find('td').text.strip()
        except AttributeError:
            continue


def find_age(soup):
    for tr in find_quest_infobox(soup).find_all('tr'):
        try:
            if tr.find('th').text.strip() == "Age":
                return 6 if tr.find('td').text.strip() == "Sixth Age" else 5
        except AttributeError:
            continue


def testing(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    # Name!
    name = get_quest_name(soup)
    print(name)

    # Get the table with the quest details. (Will help later).
    quest_details = find_quest_details(soup)

    # is_free
    is_free = find_is_free(quest_details)
    print(is_free)

    # age
    age = find_age(soup)
    print(age)

    # difficulty
    difficulty = find_difficulty_or_length(quest_details, "difficulty")
    print(difficulty)

    # length
    length = find_difficulty_or_length(quest_details, "length")
    print(length)

    # quest_points  TODO: this are more complicated / less helpful so leaving
    # them out for now

    # quests needed
    requirements = find_requirements(quest_details)
    quests = find_quests(requirements)
    print(quests)

    # Skills needed


def test_all():
    urls = ['https://runescape.wiki/w/The_Blood_Pact',
            'https://runescape.wiki/w/Cold_War',
            'https://runescape.wiki/w/The_Chosen_Commander',
            'https://runescape.wiki/w/Call_of_the_Ancestors',
            'https://runescape.wiki/w/Land_of_the_Goblins',
            'https://runescape.wiki/w/The_World_Wakes']
    for u in urls:
        print()
        testing(u)


testing('https://runescape.wiki/w/The_Chosen_Commander')
test_all()
