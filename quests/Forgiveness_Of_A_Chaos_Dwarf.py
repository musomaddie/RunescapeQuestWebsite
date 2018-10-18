import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Forgiveness_Of_A_Chaos_Dwarf(Quest):

    def __init__(self):
        super().__init__("Forgiveness of a Chaos Dwarf")
        self.age = 6
        self.difficulty = "Master"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.hunter = 61
        self.firemaking = 61
        self.strength = 69
