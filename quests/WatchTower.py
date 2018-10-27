import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class WatchTower(Quest):

    def __init__(self):
        super().__init__("Watchtower")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 4

        self.herblore = 14
        self.magic = 14
        self.thieving = 15
        self.agility = 25
        self.mining = 40
