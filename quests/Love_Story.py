import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Love_Story(Quest):

    def __init__(self):
        super().__init__("Love Story")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.magic = 77
        self.construction = 68
        self.smithing = 68
        self.crafting = 67
