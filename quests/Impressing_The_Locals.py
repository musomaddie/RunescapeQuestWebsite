import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Impressing_The_Locals(Quest):

    def __init__(self):
        super().__init__("Impressing the Locals")
        self.age = 6
        self.difficulty = "Novice"
        self.length = "Short"
        self.quest_points = 1
