import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Enlightened_Journey(Quest):

    def __init__(self):
        super().__init__("Enlightened Journey")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.firemaking = 20
        self.farming = 30
        self.crafting = 36
