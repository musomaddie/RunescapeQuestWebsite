import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Branches_Of_Darkmeyer(Quest):

    def __init__(self):
        super().__init__("The Branches of Darkmeyer")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 2

        self.woodcutting = 76
        self.fletching = 70
        self.magic = 70
        self.slayer = 67
        self.crafting = 64
        self.farming = 63
        self.agility = 63
        self.attack = 70
        self.ranged = 70
