import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Gower_Quest(Quest):

    def __init__(self):
        super().__init__("Gower Quest")
        self.free = True
        self.age = 6
        self.difficulty = "Experienced"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.other_requirements.append("34 quest points")
