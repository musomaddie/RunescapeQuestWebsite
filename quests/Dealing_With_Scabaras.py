import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Dealing_With_Scabaras(Quest):

    def __init__(self):
        super().__init__("Dealing with Scabaras")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 1

        self.firemaking = 21
        self.agility = 50
        self.thieving = 60
        self.strength = 60
