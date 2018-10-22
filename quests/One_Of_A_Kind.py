import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class One_Of_A_Kind(Quest):

    def __init__(self):
        super().__init__("One of a Kind")
        self.age = 6
        self.difficulty = "Grandmaster"
        self.length = "Long to Very Long"
        self.quest_points = 1

        self.divination = 40
        self.dungeoneering = 67
        self.summoning = 74
        self.magic = 81
