import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Eadgars_Ruse(Quest):

    def __init__(self):
        super().__init__("Eadgar's Ruse")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 1

        self.herblore = 31
        self.agility = 15
