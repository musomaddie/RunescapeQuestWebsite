import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Lost_Tribe(Quest):

    def __init__(self):
        super().__init__("The Lost Tribe")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.agility = 13
        self.mining = 17
        self.thieving = 13
