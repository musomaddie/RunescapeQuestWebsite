import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_World_Wakes(Quest):

    def __init__(self):
        super().__init__("The World Wakes")
        self.age = 5
        self.difficulty = "Grandmaster"
        self.length = "Long to Very Long"
        self.quest_points = 3
