import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Biohazard(Quest):

    def __init__(self):
        super().__init__("Biohazard")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Medium"
        self.quest_points = 3

        self.firemaking = 43
