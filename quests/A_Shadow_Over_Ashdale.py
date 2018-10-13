import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class A_Shadow_Over_Ashdale(Quest):

    def __init__(self):
        super().__init__("A Shadow Over Ashadale")
        self.age = 6
        self.free = True
