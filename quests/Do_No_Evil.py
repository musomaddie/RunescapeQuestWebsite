import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Do_No_Evil(Quest):

    def __init__(self):
        super().__init__("Do No Evil")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Very Long"
        self.quest_points = 1

        self.ranged = 50
        self.construction = 64
        self.crafting = 68
        self.magic = 70
        self.thieving = 70
        self.other_requirements.append("Must have restored Senliten to 100%")
        self.other_requirements.append("Must have led Leela to Senliten's tomb")
