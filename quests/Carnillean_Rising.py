import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Carnillean_Rising(Quest):

    def __init__(self):
        super().__init__("Carnillean Rising")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.thieving = 33
        self.construction = 31
        self.other_requirments.append("50 quest points")
