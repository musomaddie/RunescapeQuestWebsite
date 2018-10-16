import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Eyes_Of_Glouphrie(Quest):

    def __init__(self):
        super().__init__("The Eyes of Glouphrie")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 2

        self.construction = 5
        self.magic = 46
