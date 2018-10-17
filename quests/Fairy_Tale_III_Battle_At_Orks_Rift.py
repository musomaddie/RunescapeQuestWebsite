import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Fairy_Tale_III_Battle_At_Orks_Rift(Quest):

    def __init__(self):
        super().__init__("Fairy Tale III - Battle at Ork's Rift")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2

        self.magic = 59
        self.farming = 54
        self.thieving = 51
        self.summoning = 37
        self.crafting = 36
