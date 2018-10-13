import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Restless_Ghost(Quest):

    def __init__(self):
        super().__init__("The Restless Ghost")
        self.free = True
        self.age = 5
