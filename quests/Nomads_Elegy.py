import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Nomads_Elegy(Quest):

    def __init__(self):
        super().__init__("Nomad's Elegy")
        self.age = 6
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 1

        self.mining = 75
        self.construction = 75
        self.woodcutting = 75
