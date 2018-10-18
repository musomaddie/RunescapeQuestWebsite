import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Kings_Ransom(Quest):

    def __init__(self):
        super().__init__("King's Ransom")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.magic = 45
        self.defence = 65
