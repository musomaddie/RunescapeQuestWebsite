import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Legends_Quest(Quest):

    def __init__(self):
        super().__init__("Legends' Quest")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long to Very Long"
        self.quest_points = 4

        self.agility = 50
        self.crafting = 50
        self.herblore = 45
        self.magic = 56
        self.mining = 52
        self.prayer = 42
        self.smithing = 50
        self.strength = 50
        self.thieving = 50
        self.woodcutting = 50
        self.other_requirements.append("107 quest points")
