import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Land_Of_The_Goblins(Quest):

    def __init__(self):
        super().__init__("Land of the Goblins")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long"
        self.quest_points = 1

        self.prayer = 30
        self.agility = 36
        self.fishing = 36
        self.thieving = 36
        self.herblore = 37
