import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class A_Clockwork_Syringe(Quest):

    def __init__(self):
        super().__init__("A Clockwork Syringe")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long"
        self.quest_points = 1

        self.dungeoneering = 50
        self.slayer = 61
        self.construction = 62
        self.summoning = 62
        self.smithing = 74
        self.thieving = 74
        self.defence = 76
