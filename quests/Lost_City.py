import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Lost_City(Quest):

    def __init__(self):
        super().__init__("Lost City")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 3

        self.crafting = 31
        self.woodcutting = 36
