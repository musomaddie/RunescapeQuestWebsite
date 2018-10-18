import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Forgettable_Tale(Quest):

    def __init__(self):
        super().__init__("Forgettable Tale...")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2

        self.cooking = 22
        self.farming = 17
