import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Lunar_Diplomacy(Quest):

    def __init__(self):
        super().__init__("Lunar Diplomacy")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 2

        self.crafting = 61
        self.defence = 40
        self.firemaking = 49
        self.mining = 60
        self.herblore = 5
        self.runecrafting = 14
        self.magic = 65
        self.woodcutting = 55
