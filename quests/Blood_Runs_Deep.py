import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Blood_Runs_Deep(Quest):

    def __init__(self):
        super().__init__("Blood Runs Deep")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 2

        self.attack = 75
        self.strength = 75
        self.slayer = 65
        self.other_requirements.append("Must have claimed the reward for completing the Hard Fremennik Province Tasks")
