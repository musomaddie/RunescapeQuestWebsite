import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Phite_Club(Quest):

    def __init__(self):
        super().__init__("'Phite Club")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Short"
        self.quest_points = 1

        self.other_requirements.append("Rank 9 in overall Menaphos reputation")
