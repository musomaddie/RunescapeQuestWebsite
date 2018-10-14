import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Knights_Sword(Quest):

    def __init__(self):
        super().__init__("The Knights Sword")
        self.age = 5
        self.free = True
        self.difficulty = "Intermediate"
        self.length = "Short"
        self.quest_points = 1

        self.mining = 10
