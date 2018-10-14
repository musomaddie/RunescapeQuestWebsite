import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Another_Slice_Of_Ham(Quest):

    def __init__(self):
        super().__init__("Another Slice of H.A.M.")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.attack = 15
        self.prayer = 25
