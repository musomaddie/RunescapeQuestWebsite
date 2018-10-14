import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Death_Of_Chivalry(Quest):

    def __init__(self):
        super().__init__("The Death of Chivalry")
        self.free = True
        self.age = 6
        self.difficulty = "Novice"
        self.length = "Long"
        self.quest_points = 3
