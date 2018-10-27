import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Within_The_Light(Quest):

    def __init__(self):
        super().__init__("Within The Light")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 2

        self.agility = 69
        self.fletching = 70
        self.ranged = 75
        self.woodcutting = 75
