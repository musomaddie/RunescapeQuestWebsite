import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Chosen_Commander(Quest):

    def __init__(self):
        super().__init__("The Chosen Commander")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Long to Very Long"
        self.quest_points = 3

        self.agility = 46
        self.strength = 46
        self.thieving = 46
