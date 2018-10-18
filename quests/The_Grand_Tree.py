import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Grand_Tree(Quest):

    def __init__(self):
        super().__init__("The Grand Tree")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 5
