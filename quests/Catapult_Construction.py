import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Catapult_Construction(Quest):

    def __init__(self):
        super().__init__("Catapult Construction")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Short to Medium"
        self.quest_points = 2

        self.fletching = 42
        self.construction = 44
