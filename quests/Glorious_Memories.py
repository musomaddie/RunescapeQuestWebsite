import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Glorious_Memories(Quest):

    def __init__(self):
        super().__init__("Glorious Memories")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium"
        self.quest_points = 1

        self.magic = 57
        self.agility = 50
        self.herblore = 43
        self.hunter = 41
