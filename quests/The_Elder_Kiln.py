import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Elder_Kiln(Quest):

    def __init__(self):
        super().__init__("The Elder Kiln")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 2

        self.magic = 75
        self.agility = 60
        self.mining = 41
