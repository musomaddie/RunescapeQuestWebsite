import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class TokTz_Ket_Dill(Quest):

    def __init__(self):
        super().__init__("TokTz-Ket-Dill")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long to Very Long"
        self.quest_points = 1

        self.attack = 50
        self.construction = 50
        self.crafting = 43
        self.mining = 41
        self.strength = 45
