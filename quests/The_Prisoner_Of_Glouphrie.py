import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Prisoner_Of_Glouphrie(Quest):

    def __init__(self):
        super().__init__("The Prisoner of Glouphrie")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium"
        self.quest_points = 1

        self.agility = 64
        self.construction = 62
        self.runecrafting = 61
        self.thieving = 64
