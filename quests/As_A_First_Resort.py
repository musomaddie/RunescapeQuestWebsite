import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class As_A_First_Resort(Quest):

    def __init__(self):
        super().__init__("As a First Resort")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 1

        self.hunter = 48
        self.firemaking = 51
        self.woodcutting = 58
