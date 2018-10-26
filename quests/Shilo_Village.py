import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Shilo_Village(Quest):

    def __init__(self):
        super().__init__("Shilo Village")
        self.age = 6
        self.difficulty = "Experienced"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.crafting = 20
        self.agility = 32
