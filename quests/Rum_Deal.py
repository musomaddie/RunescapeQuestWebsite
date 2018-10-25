import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Rum_Deal(Quest):

    def __init__(self):
        super().__init__("Rum Deal")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2

        self.farming = 40
        self.crafting = 42
        self.prayer = 47
        self.fishing = 50
        self.slayer = 42
