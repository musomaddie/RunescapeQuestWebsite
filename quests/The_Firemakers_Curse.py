import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Firemakers_Curse(Quest):

    def __init__(self):
        super().__init__("The Firemaker's Curse")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Very Long"
        self.quest_points = 2

        self.firemaking = 74
        self.constitution = 76
        self.agility = 64
