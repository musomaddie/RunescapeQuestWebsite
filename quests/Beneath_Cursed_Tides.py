import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Beneath_Cursed_Tides(Quest):

    def __init__(self):
        super().__init__("Beneath Cursed Tides")
        self.age = 6
        self.free = True
        self.difficulty = "Intermediate"
        self.quest_points = 1
        self.length = "Medium"

        self.attack = 30
        self.strength = 30
        self.magic = 30
        self.mining = 30
        self.smithing = 30
        self.woodcutting = 30
        self.firemaking = 30
        self.cooking = 30
