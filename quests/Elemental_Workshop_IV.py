import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Elemental_Workshop_IV(Quest):

    def __init__(self):
        super().__init__("Elemental Workshop IV")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2

        self.crafting = 41
        self.runecrafting = 39
        self.thieving = 39
        self.defence = 40
        self.smithing = 42
