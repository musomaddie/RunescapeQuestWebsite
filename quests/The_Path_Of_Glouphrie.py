import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Path_Of_Glouphrie(Quest):

    def __init__(self):
        super().__init__("The Path of Glouphrie")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 1

        self.strength = 60
        self.thieving = 56
        self.slayer = 56
        self.ranged = 47
        self.agility = 45

