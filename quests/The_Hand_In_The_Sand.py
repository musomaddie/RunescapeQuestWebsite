import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Hand_In_The_Sand(Quest):

    def __init__(self):
        super().__init__("The Hand in the Sand")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.thieving = 17
        self.crafting = 49
