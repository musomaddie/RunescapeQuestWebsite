import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Lord_Of_Vampyrium(Quest):

    def __init__(self):
        super().__init__("The Lord of Vampyrium")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long to Very Long"
        self.quest_points = 2

        self.attack = 75
        self.defence = 75
        self.strength = 75
        self.constitution = 75
        self.construction = 79
        self.slayer = 78
        self.hunter = 76
