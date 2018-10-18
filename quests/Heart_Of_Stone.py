import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Heart_Of_Stone(Quest):

    def __init__(self):
        super().__init__("Heart Of Stone")
        self.age = 6
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 1

        self.runecrafting = 25
        self.magic = 35
