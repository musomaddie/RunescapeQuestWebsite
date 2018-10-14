import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Ernest_The_Chicken(Quest):

    def __init__(self):
        super().__init__("Ernest The Chicken")
        self.free = True
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Medium"
        self.quest_points = 4
