import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Fremennik_Isles(Quest):

    def __init__(self):
        super().__init__("The Fremennik Isles")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 1

        self.construction = 20
        self.crafting = 46
        self.agility = 40
        self.woodcutting = 56
