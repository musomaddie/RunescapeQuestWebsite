import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Scorpion_Catcher(Quest):

    def __init__(self):
        super().__init__("Scorpion Catcher")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Short"
        self.quest_points = 1

        self.prayer = 31
        self.other_requirements.append("Bar Crawl")
