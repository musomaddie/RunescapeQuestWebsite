import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Some_Like_It_Cold(Quest):

    def __init__(self):
        super().__init__("Some Like It Cold")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long to Very Long"
        self.quest_points = 1

        self.fishing = 65
        self.crafting = 46
        self.construction = 50
        self.thieving = 50
