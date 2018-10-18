import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Fishing_Contest(Quest):

    def __init__(self):
        super().__init__("Fishing Contest")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Short"
        self.quest_points = 1

        self.fishing = 10
