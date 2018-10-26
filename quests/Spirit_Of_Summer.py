import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Spirit_Of_Summer(Quest):

    def __init__(self):
        super().__init__("Spirit of Summer")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 1

        self.summoning = 19
        self.farming = 26
        self.prayer = 35
        self.construction = 40
