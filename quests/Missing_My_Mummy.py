import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Missing_My_Mummy(Quest):

    def __init__(self):
        super().__init__("Missing My Mummy")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.construction = 35
        self.cooking = 35
        self.crafting = 35
        self.magic = 35
        self.prayer = 35
