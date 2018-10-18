import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Grim_Tales(Quest):

    def __init__(self):
        super().__init__("Grim Tales")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium"
        self.quest_points = 1

        self.farming = 45
        self.herblore = 52
        self.thieving = 58
        self.agility = 59
        self.woodcutting = 71
