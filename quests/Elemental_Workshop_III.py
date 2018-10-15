import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Elemental_Workshop_III(Quest):

    def __init__(self):
        super().__init__("Elemental Workshop III")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.defence = 33
        self.mining = 20
        self.smithing = 30
