import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Perils_Of_Ice_Mountain(Quest):

    def __init__(self):
        super().__init__("Perils of Ice Mountain")
        self.free = True
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Medium"
        self.quest_points = 1

        self.farming = 5
        self.hunting = 5
        self.thieving = 5
