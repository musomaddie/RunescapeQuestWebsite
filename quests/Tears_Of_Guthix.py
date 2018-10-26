import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Tears_Of_Guthix(Quest):

    def __init__(self):
        super().__init__("Tears of Guthix")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Short"
        self.quest_points = 1

        self.firemaking = 49
        self.mining = 20
        self.crafting = 20
