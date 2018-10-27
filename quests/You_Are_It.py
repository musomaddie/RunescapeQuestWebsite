import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class You_Are_It(Quest):

    def __init__(self):
        super().__init__("You Are It")
        self.age = 6
        self.difficulty = "Intermediate"
        self.length = "Short"
        self.quest_points = 1
