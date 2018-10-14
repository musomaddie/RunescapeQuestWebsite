import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Bringing_Home_The_Bacon(Quest):

    def __init__(self):
        super().__init__("Bringing Home the Bacon")
        self.age = 6
        self.difficulty = "Novice"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.farming = 14
        self.summoning = 14
        self.construction = 14
