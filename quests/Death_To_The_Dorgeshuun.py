import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Death_To_The_Dorgeshuun(Quest):

    def __init__(self):
        super().__init__("Death to the Dorgeshuun")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.thieving = 23
        self.agility = 23
