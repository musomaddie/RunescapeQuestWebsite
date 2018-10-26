import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Shadow_Of_The_Storm(Quest):

    def __init__(self):
        super().__init__("Shadow of the Storm")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 1

        self.crafting = 30
