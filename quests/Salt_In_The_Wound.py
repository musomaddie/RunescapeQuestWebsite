import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Salt_In_The_Wound(Quest):

    def __init__(self):
        super().__init__("Salt In The Wound")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2

        self.defence = 60
        self.constitution = 50
        self.herblore = 47
        self.summoning = 45
        self.dungeoneering = 35
