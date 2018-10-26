import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Temple_Of_Ikov(Quest):

    def __init__(self):
        super().__init__("Temple of Ikov")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 1

        self.thieving = 42
        self.ranged = 40
