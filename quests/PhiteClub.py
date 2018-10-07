import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Phite_Club(Quest):

    def __init__(self):
        super().__init__("'Phite Club")
        print(self.name)
        print(self.agility)

Phite_Club()
