import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class In_Pyre_Need(Quest):

    def __init__(self):
        super().__init__("In Pyre Need")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Short to Medium"
        self.quest_points = 1

        self.firemaking = 55
        self.crafting = 52
        self.fletching = 53
