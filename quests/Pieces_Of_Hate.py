import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Pieces_Of_Hate(Quest):

    def __init__(self):
        super().__init__("Pieces of Hate")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 2

        self.construction = 81
        self.firemaking = 82
        self.agility = 83
        self.thieving = 85
