import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class One_Piercing_Note(Quest):

    def __init__(self):
        super().__init__("One Piercing Note")
        self.age = 5
        self.free = True
        self.difficulty = "Novice"
        self.length = "Medium to Long"
        self.quest_points = 2
