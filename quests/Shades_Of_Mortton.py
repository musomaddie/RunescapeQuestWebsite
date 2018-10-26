import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Shades_Of_Mortton(Quest):

    def __init__(self):
        super().__init__("Shades of Mort'ton")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 3

        self.crafting = 20
        self.firemaking = 5
        self.herblore = 15
