import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class A_Souls_Bane(Quest):

    def __init__(self):
        super().__init__("A Soul's Bane")
        self.free = True
        self.age = 5
