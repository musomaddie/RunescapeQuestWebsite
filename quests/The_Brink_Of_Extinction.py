import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Brink_Of_Extinction(Quest):

    def __init__(self):
        super().__init__("The Brink of Extinction")
        self.age = 5
        self.difficulty = "Grandmaster"
        self.length = "Medium to Long"
        self.quest_points = 3

        self.defence = 80
        self.smithing = 80
        self.mining = 72
