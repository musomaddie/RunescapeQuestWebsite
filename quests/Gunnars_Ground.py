import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Gunnars_Ground(Quest):

    def __init__(self):
        super().__init__("Gunnar's Ground")
        self.age = 5
        self.free = True
        self.difficulty = "Novice"
        self.length = "Short to Medium"
        self.quest_points = 5

        self.crafting = 5

