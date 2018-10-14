import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Between_A_Rock(Quest):

    def __init__(self):
        super().__init__("Between a Rock...")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2

        self.defence = 30
        self.mining = 40
        self.smithing = 50
