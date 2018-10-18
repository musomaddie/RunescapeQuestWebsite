import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Great_Brain_Robbery(Quest):

    def __init__(self):
        super().__init__("The Great Brain Robbery")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.crafting = 16
        self.construction = 30
        self.prayer = 50
