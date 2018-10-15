import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Desert_Treasure(Quest):

    def __init__(self):
        super().__init__("Desert Treasure")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Very Long"
        self.quest_points = 3

        self.slayer = 10
        self.firemaking = 50
        self.magic = 50
        self.thieving = 53
        self.mining = 50
