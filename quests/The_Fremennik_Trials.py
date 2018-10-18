import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Fremennik_Trials(Quest):

    def __init__(self):
        super().__init__("The Fremennik Trials")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 3

        self.crafting = 40
        self.fletching = 25
        self.woodcutting = 40
