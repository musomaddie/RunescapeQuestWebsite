import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Enakhras_Lament(Quest):

    def __init__(self):
        super().__init__("Enakhra's Lament")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2

        self.crafting = 50
        self.firemaking = 45
        self.magic = 13
