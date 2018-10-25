import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Ritual_Of_The_Mahjarrat(Quest):

    def __init__(self):
        super().__init__("Ritual of the Mahjarrat")
        self.age = 5
        self.difficulty = "Grandmaster"
        self.length = "Very, Very Long"
        self.quest_points = 3

        self.crafting = 76
        self.agility = 77
        self.mining = 76
