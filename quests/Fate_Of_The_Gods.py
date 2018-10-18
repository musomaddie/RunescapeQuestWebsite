import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Fate_Of_The_Gods(Quest):

    def __init__(self):
        super().__init__("Fate of the Gods")
        self.age = 6
        self.difficulty = "Grandmaster"
        self.length = "Long to Very Long"
        self.quest_points = 2

        self.summoning = 67
        self.agility = 73
        self.divination = 75
        self.slayer = 76
        self.magic = 79
