import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Our_Man_In_The_North(Quest):

    def __init__(self):
        super().__init__("Our Man in the North")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Short to Medium"
        self.quest_points = 1
