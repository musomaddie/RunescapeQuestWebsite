import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Curse_Of_Arrav(Quest):

    def __init__(self):
        super().__init__("The Curse of Arrav")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.slayer = 37
        self.summoning = 41
        self.agility = 61
        self.ranged = 64
        self.strength = 64
        self.mining = 64
        self.thieving = 66
        self.other_requirements.append("Senliten fully restored")
