import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Recipe_For_Disaster(Quest):

    def __init__(self):
        super().__init__("Recipe for Disaster")
        self.age = 5
        self.difficulty = "Special"
        self.length = "Very, Very Long"
        self.quest_points = 10

        self.cooking = 70
        self.firemaking = 20
        self.agility = 48
        self.other_requirements.append("176 Quest Points")
