import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Call_Of_The_Ancestors(Quest):

    def __init__(self):
        super().__init__("Call of the Ancestors")
        self.age = 6
        self.difficulty = "Novice"
        self.length = "Medium"
        self.quest_points = 1
