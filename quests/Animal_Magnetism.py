import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Animal_Magnetism(Quest):

    def __init__(self):
        super().__init__("Animal Magnetism")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.crafting = 19
        self.slayer = 18
        self.ranged = 30
        self.woodcutting = 35
