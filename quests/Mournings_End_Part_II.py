import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Mournings_End_Part_II(Quest):

    def __init__(self):
        super().__init__("Mourning's End Part II")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Very Long"
        self.quest_points = 2
