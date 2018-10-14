import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Big_Chompy_Bird_Hunting(Quest):

    def __init__(self):
        super().__init__("Big Chompy Bird Hunting")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 2

        self.cooking = 30
        self.ranged = 30
        self.fletching = 5
