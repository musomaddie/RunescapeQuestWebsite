import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Deadliest_Catch(Quest):

    def __init__(self):
        super().__init__("Deadliest Catch")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Short to Medium"
        self.quest_points = 1

        self.herblore = 3
        self.hunter = 67
        self.thieving = 70
        self.fishing = 70
