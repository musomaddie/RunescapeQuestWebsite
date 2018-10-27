import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Underground_Pass(Quest):

    def __init__(self):
        super().__init__("Underground Pass")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long to Very Long"
        self.quest_points = 5

        self.ranged = 25
