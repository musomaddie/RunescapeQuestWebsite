import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Swan_Song(Quest):

    def __init__(self):
        super().__init__("Swan Song")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.magic = 66
        self.cooking = 62
        self.fishing = 62
        self.smithing = 45
        self.firemaking = 42
        self.crafting = 40
        self.other_requirements.append("101 quest points")
