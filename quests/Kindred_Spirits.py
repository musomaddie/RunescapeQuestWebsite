import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Kindred_Spirits(Quest):

    def __init__(self):
        super().__init__("Kindred Spirits")
        self.age = 6
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 1

        self.agility = 60
        self.crafting = 60
        self.herblore = 60
        self.smithing = 60
