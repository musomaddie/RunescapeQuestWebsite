import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Birthright_Of_The_Dwarves(Quest):

    def __init__(self):
        super().__init__("Birthright of the Dwarves")
        self.age = 6
        self.difficulty = "Grandmaster"
        self.length = "Very Long"
        self.quest_points = 2

        self.mining = 80
        self.smithing = 82
        self.strength = 85
