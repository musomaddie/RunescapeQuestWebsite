import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Jack_Of_Spades(Quest):

    def __init__(self):
        super().__init__("The Jack of Spades")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Short to Medium"
        self.quest_points = 1
