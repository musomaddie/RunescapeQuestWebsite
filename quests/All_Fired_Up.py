import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class All_Fired_Up(Quest):

    def __init__(self):
        super().__init__("All Fired Up")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Short to Medium"
        self.quest_points = 1

        self.firemaking = 43
