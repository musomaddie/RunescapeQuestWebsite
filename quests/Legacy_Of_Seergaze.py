import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Legacy_Of_Seergaze(Quest):

    def __init__(self):
        super().__init__("Legacy of Seergaze")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long to Very Long"
        self.quest_points = 2

        self.construction = 20
        self.agility = 29
        self.slayer = 31
        self.mining = 35
        self.firemaking = 40
        self.crafting = 47
        self.magic = 49
