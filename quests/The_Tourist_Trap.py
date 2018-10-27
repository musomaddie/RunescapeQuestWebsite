import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Tourist_Trap(Quest):

    def __init__(self):
        super().__init__("The Tourist Trap")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.fletching = 10
        self.smithing = 20
