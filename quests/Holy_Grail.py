import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Holy_Grail(Quest):

    def __init__(self):
        super().__init__("Holy Grail")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Short to Medium"
        self.quest_points = 2

        self.attack = 30
