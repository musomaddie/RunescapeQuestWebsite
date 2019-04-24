import requests
from bs4 import BeautifulSoup
import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("")])
from quests.QuestInfo import Quest


valid_skills = {'Agility',
                'Attack',
                'Constitution',
                'Construction',
                'Cooking',
                'Crafting',
                'Defence',
                'Divination',
                'Dungeoneering',
                'Farming',
                'Firemaking',
                'Fishing',
                'Fletching',
                'Herblore',
                'Hunter',
                'Magic',
                'Mining',
                'Prayer',
                'Ranged',
                'Runecrafting'
                'Slayer',
                'Smithing',
                'Strength',
                'Summoning',
                'Thieving',
                'Woodcutting'}


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
    this_quest = next(quests.children).find('ul')
    quests = []
    for child in this_quest:
        quests.append(child.contents[0].text)
    return quests


def find_skills(requirements):
    skills_maybe = []
    for c in requirements.children:
        if c.name == "ul":
            skills_maybe.append(c)
    actual_skills = {}

    for s in skills_maybe:
        try:
            level, skill = s.text.split("  ")
            if skill in valid_skills:
                actual_skills[skill] = level
        except (TypeError, ValueError):
            continue
    return actual_skills


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


def create_quest(url, all_quests, quest_to_children):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    quest_details = find_quest_details(soup)
    requirements = find_requirements(quest_details)
    name = get_quest_name(soup)

    is_free = find_is_free(quest_details)
    age = find_age(soup)
    difficulty = find_difficulty_or_length(quest_details, "difficulty")
    length = find_difficulty_or_length(quest_details, "length")
    quests = find_quests(requirements)
    skills = find_skills(requirements)

    quest_to_children[name] = quests
    all_quests[name] = Quest(name, is_free, age, difficulty, length, skills)