import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Elemental_Workshop_I(Quest):

    def __init__(self):
        super().__init__("Elemental Workshop I")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Short"
        self.quest_points = 1

        self.mining = 20
        self.smithing = 20
        self.crafting = 20
