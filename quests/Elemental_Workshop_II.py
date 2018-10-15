import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Elemental_Workshop_II(Quest):

    def __init__(self):
        super().__init__("Elemental Workshop II")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.magic = 20
        self.smithing = 30
