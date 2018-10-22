import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class One_Small_Favour(Quest):

    def __init__(self):
        super().__init__("One Small Favour")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 2

        self.herblore = 18
        self.crafting = 25
        self.smithing = 30
        self.agility = 36
