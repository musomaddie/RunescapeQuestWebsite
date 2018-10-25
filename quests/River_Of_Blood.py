import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class River_Of_Blood(Quest):

    def __init__(self):
        super().__init__("River of Blood")
        self.age = 5
        self.difficulty = "Grandmaster"
        self.length = "Long to Very Long"
        self.quest_points = 3

        self.herblore = 80
        self.constitution = 80
        self.attack = 78
        self.ranged = 78
        self.magic = 78
        self.firemaking = 76
        self.fletching = 75
        self.mining = 72
