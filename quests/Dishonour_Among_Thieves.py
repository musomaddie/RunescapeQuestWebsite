import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Dishonour_Among_Thieves(Quest):

    def __init__(self):
        super().__init__("Dishonour Among Thieves")
        self.age = 6
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2

        self.agility = 30
        self.thieving = 30
        self.other_requirements.append("Access to Morytania")
