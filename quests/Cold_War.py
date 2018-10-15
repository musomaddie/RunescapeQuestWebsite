import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Cold_War(Quest):

    def __init__(self):
        super().__init__("Cold War")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 1

        self.hunter = 10
        self.construction = 34
        self.crafting = 30
        self.agility = 30
        self.thieving = 15
