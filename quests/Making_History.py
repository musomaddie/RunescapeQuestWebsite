import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Making_History(Quest):

    def __init__(self):
        super().__init__("Making History")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 3

        self.crafting = 24
        self.smithing = 40
        self.mining = 40
