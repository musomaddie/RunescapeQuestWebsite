import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class While_Guthix_Sleeps(Quest):

    def __init__(self):
        super().__init__("While Guthix Sleeps")
        self.age = 5
        self.difficulty = "Grandmaster"
        self.length = "Very, Very Long"
        self.quest_points = 5

        self.summoning = 23
        self.hunter = 55
        self.thieving = 60
        self.defence = 65
        self.farming = 65
        self.herblore = 65
        self.magic = 75
        self.other_requirements.append("270 quest points")
        self.other_requirements.append("Be eligible for entry to the Warriors Guild")
        self.other_requirements.append("Have defeated Bork in the Chaos Tunnels")
