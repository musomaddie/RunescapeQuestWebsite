import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Dimension_Of_Disaster(Quest):

    def __init__(self):
        super().__init__("Dimension of Disaster")
        self.age = 6
        self.difficulty = "Special"
        self.length = "Very, Very Long"
        self.quest_points = 10
