import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Regicide(Quest):

    def __init__(self):
        super().__init__("Regicide")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 3

        self.agility = 56
        self.crafting = 10
