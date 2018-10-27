import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Void_Stares_Back(Quest):

    def __init__(self):
        super().__init__("The Void Stares Back")
        self.age = 5
        self.difficulty = "Grandmaster"
        self.length = "Long"
        self.quest_points = 1

        self.magic = 80
        self.attack = 78
        self.strength = 78
        self.firemaking = 71
        self.construction = 70
        self.crafting = 70
        self.smithing = 70
        self.summoning = 55
        self.defence = 25
