import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Heros_Welcome(Quest):

    def __init__(self):
        super().__init__("Hero's Welcome")
        self.age = 6
        self.difficulty = "Experienced"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.divination = 60
        self.mining = 67
        self.slayer = 62
        self.smithing = 67
        self.other_requirements.append("Completed all of Otto Godblessed's Barbarian Training activities")
