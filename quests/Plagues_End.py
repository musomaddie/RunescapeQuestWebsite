import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Plagues_End(Quest):

    def __init__(self):
        super().__init__("Plague's End")
        self.age = 6
        self.difficulty = "Grandmaster"
        self.length = "Long to very Long"
        self.quest_points = 2

        self.agility = 75
        self.construction = 75
        self.crafting = 75
        self.dungeoneering = 75
        self.herblore = 75
        self.mining = 75
        self.prayer = 75
        self.ranged = 75
        self.summoning = 75
        self.woodcutting = 75
