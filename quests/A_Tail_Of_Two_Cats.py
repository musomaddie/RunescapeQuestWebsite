import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class A_Tail_Of_Two_Cats(Quest):

    def __init__(self):
        super().__init__("A Tail of Two Cats")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2
