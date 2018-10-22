import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class My_Arms_Big_Adventure(Quest):

    def __init__(self):
        super().__init__("My Arm's Big Adventure")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium to Long"
        self.quest_points = 1

        self.woodcutting = 10
        self.farming = 20
        self.other_requirements.append("60%% favour with the people of Tai Bwo Wannai Village")
