import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Horror_From_The_Deep(Quest):

    def __init__(self):
        super().__init__("Horror from the Deep")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2

        self.agility = 35
        self.other_requirements.append("Bar Crawl")
