import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Tale_Of_The_Muspah(Quest):

    def __init__(self):
        super().__init__("The Tale of the Muspah")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Medium"
        self.quest_points = 1

        self.firemaking = 6
        self.mining = 8
        self.magic = 10
        self.woodcutting = 10
