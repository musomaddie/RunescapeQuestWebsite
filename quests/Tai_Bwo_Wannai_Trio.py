import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Tai_Bwo_Wannai_Trio(Quest):

    def __init__(self):
        super().__init__("Tai Bwo Wannai Trio")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2

        self.agility = 15
        self.fishing = 5
        self.cooking = 30
