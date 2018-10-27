import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class A_Void_Dance(Quest):

    def __init__(self):
        super().__init__("A Void Dance")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 1

        self.hunter = 46
        self.construction = 47
        self.mining = 47
        self.summoning = 48
        self.herblore = 49
        self.woodcutting = 52
        self.thieving = 54
