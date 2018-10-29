import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Mighty_Fall(Quest):
    def __init__(self):
        super().__init__("The Mighty Fall")
        self.age = 6
        self.difficulty = "Master"
        self.length = "Long to Very Long"
        self.quest_points = 2

        self.slayer = 69
        self.defence = 72
        self.constitution= 78
        self.attack = 79
        self.strength = 79
        self.other_requirements.append("Chaos Tunnels: The Hunt for Surok")
