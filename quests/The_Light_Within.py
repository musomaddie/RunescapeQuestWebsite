import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Light_Within(Quest):

    def __init__(self):
        super().__init__("The Light Within")
        self.age = 6
        self.difficulty = "Grandmaster"
        self.length = "Long"
        self.quest_points = 2

        self.agility = 80
        self.crafting = 80
        self.divination = 80
        self.herblore = 80
        self.prayer = 80
        self.slayer = 80
        self.woodcutting = 80
