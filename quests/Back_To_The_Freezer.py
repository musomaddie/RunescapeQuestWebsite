import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Back_To_The_Freezer(Quest):

    def __init__(self):
        super().__init__("Back to the Freezer")
        self.age = 6
        self.difficulty = "Master"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.slayer = 37
        self.runecrafting = 45
        self.divination = 50


