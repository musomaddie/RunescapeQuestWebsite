import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Summers_End(Quest):

    def __init__(self):
        super().__init__("Summer's End")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.summoning = 23
        self.hunter = 35
        self.woodcutting = 37
        self.mining = 45
        self.firemaking = 47
        self.prayer = 55
