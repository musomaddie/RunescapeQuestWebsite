import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Evil_Daves_Big_Day_Out(Quest):

    def __init__(self):
        super().__init__("Evil Dave's Big Day Out")
        self.age = 6
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 2

        self.agility = 30
        self.cooking = 30
        self.herblore = 30
        self.magic = 30
