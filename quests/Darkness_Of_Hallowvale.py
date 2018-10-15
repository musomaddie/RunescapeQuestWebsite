import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Darkness_Of_Hallowvale(Quest):

    def __init__(self):
        super().__init__("Darkness of Hallowvale")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Very Long"
        self.quest_points = 2

        self.construction = 5
        self.mining = 20
        self.thieving = 22
        self.agility = 26
        self.crafting = 32
        self.magic = 33
        self.strength = 40
