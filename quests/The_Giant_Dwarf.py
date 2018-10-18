import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Giant_Dwarf(Quest):

    def __init__(self):
        super().__init__("The Giant Dwarf")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.crafting = 12
        self.firemaking = 16
        self.magic = 33
        self.thieving = 14
