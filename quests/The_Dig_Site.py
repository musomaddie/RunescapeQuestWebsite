import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Dig_Site(Quest):

    def __init__(self):
        super().__init__("The Dig Site")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2

        self.thieving = 25
        self.agility = 10
        self.herblore = 10
