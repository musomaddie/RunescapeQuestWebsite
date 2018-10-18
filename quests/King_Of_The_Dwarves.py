import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class King_Of_The_Dwarves(Quest):

    def __init__(self):
        super().__init__("King of the Dwarves")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.mining = 68
        self.smithing = 70
        self.strength = 77
