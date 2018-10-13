import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Wolf_Whistle(Quest):

    def __init__(self):
        super().__init__("Wolf Whistle")
        self.free = True
        self.age = 5
