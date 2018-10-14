import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Priest_In_Peril(Quest):

    def __init__(self):
        super().__init__("Priest In Peril")
        self.age = 5
        self.free = True
        self.difficulty = "Novice"
        self.length = "Medium"
        self.quest_points = 1
