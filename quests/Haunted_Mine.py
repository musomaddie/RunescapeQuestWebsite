import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Haunted_Mine(Quest):

    def __init__(self):
        super().__init__("Haunted Mine")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 2

        self.agility = 15
        self.crafting = 35
