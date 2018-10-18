import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Hunt_For_Red_Raktuber(Quest):

    def __init__(self):
        super().__init__("Hunt for Red Raktuber")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 1

        self.thieving = 38
        self.construction = 45
        self.hunter = 45
