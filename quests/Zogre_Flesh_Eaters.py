import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Zogre_Flesh_Eaters(Quest):

    def __init__(self):
        super().__init__("Zogre Flesh Eaters")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.smithing = 4
        self.herblore = 8
        self.strength = 20
        self.ranged = 30
        self.fletching = 30
