import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Tree_Gnome_Village(Quest):

    def __init__(self):
        super().__init__("Tree Gnome Village")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 2
