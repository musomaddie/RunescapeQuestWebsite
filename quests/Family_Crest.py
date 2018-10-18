import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Family_Crest(Quest):

    def __init__(self):
        super().__init__("Family Crest")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 1

        self.crafting = 40
        self.smithing = 40
        self.mining = 40
        self.magic = 59
