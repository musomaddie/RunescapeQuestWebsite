import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Nomads_Requiem(Quest):

    def __init__(self):
        super().__init__("Nomad's Requiem")
        self.age = 5
        self.difficulty = "Grandmaster"
        self.length = "Long"
        self.quest_points = 3

        self.magic = 75
        self.prayer = 70
        self.mining = 66
        self.hunter = 65
        self.construction = 60
        self.other_requirements.append("Knight Waves training Ground")
        self.other_requirements.append("Completed Soul Wars tutorial")
