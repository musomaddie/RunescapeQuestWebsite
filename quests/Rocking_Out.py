import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Rocking_Out(Quest):

    def __init__(self):
        super().__init__("Rocking Out")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long to Very Long"
        self.quest_points = 2

        self.agility = 60
        self.thieving = 63
        self.crafting = 66
        self.smithing = 69
