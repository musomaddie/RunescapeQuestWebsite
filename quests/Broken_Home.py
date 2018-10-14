import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Broken_Home(Quest):

    def __init__(self):
        super().__init__("Broken Home")
        self.free = True
        self.age = 6
        self.difficulty = "Novice"
        self.length = "Medium to Long"
        self.quest_points = 1
