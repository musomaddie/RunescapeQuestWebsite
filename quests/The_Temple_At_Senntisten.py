import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class The_Temple_At_Senntisten(Quest):

    def __init__(self):
        super().__init__("The Temple at Senntisten")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.prayer = 50
        self.other_requirements.append("125 Kudos from the Varrock Museum")
