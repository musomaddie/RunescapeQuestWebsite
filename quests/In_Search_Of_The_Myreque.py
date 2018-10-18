import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class In_Search_Of_The_Myreque(Quest):

    def __init__(self):
        super().__init__("In Search of the Myreque")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Short"
        self.quest_points = 2

        self.agility = 25
