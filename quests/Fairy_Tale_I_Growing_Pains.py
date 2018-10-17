import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Fairy_Tale_I_Growing_Pains(Quest):

    def __init__(self):
        super().__init__("Fairy Tale I - Growing Pains")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2
