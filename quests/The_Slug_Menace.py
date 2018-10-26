import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Slug_Menace(Quest):

    def __init__(self):
        super().__init__("The Slug Menace")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.crafting = 30
        self.runecrafting = 30
        self.slayer = 30
        self.thieving = 30
