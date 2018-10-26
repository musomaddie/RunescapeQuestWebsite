import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Sliskes_Endgame(Quest):

    def __init__(self):
        super().__init__("Sliske's Endgame")
        self.age = 6
        self.difficulty = "Grandmaster"
        self.length = "Very Long"
        self.quest_points = 3
