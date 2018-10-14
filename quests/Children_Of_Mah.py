import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Children_Of_Mah(Quest):

    def __init__(self):
        super().__init__("Children of Mah")
        self.age = 6
        self.difficulty = "Grandmaster"
        self.length = "Medium to Long"
        self.quest_points = 2
