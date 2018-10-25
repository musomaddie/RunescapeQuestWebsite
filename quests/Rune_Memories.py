import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Rune_Memories(Quest):

    def __init__(self):
        super().__init__("Rune Memories")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Long"
        self.quest_points = 1

        self.magic = 27
        self.runecrafting = 20
        self.construction = 25
