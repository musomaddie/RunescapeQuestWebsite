import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Devious_Minds(Quest):

    def __init__(self):
        super().__init__("Devious Minds")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 1

        self.runecrafting = 50
        self.fletching = 50
        self.smithing = 65
