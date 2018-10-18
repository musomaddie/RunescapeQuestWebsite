import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class In_Aid_Of_The_Myreque(Quest):

    def __init__(self):
        super().__init__("In Aid of the Myreque")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2

        self.crafting = 25
        self.magic = 7
        self.mining = 15
