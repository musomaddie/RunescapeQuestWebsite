import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Quiet_Before_The_Swarm(Quest):

    def __init__(self):
        super().__init__("Quiet Before the Swarm")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long to Very Long"
        self.quest_points = 1

        self.attack = 35
        self.strength = 42
