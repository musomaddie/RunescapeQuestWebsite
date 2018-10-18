import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Jungle_Potion(Quest):

    def __init__(self):
        super().__init__("Jungle Potion")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Short"
        self.quest_points = 1

        self.herblore = 3
