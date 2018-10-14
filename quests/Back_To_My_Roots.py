import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Back_To_My_Roots(Quest):

    def __init__(self):
        super().__init__("Back to my Roots")
        self.age = 5
        self.agility = 55
        self.farming = 53
        self.slayer = 59
        self.woodcutting = 72
