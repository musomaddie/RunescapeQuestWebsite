import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Heroes_Quest(quest):

    def __init__(self):
        super().__init__("Heroes' Quest")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 1

        self.cooking = 53
        self.fishing = 53
        self.herblore = 25
        self.defence = 25
        self.mining = 50
