import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Vampyre_Slayer(Quest):

    def __init__(self):
        super().__init__("Vampyre Slayer")
        self.free = True
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Short"
        self.quest_points = 3
