import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Rune_Mysteries(Quest):

    def __init__(self):
        super().__init__("Rune Mysteries")
        self.age = 5
        self.free = True
        self.difficulty = "Novice"
        self.length = "Medium to Long"
        self.quest_points = 1
