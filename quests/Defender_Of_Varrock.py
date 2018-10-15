import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Defender_Of_Varrock(Quest):

    def __init__(self):
        super().__init__("Defender of Varrock")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium to Long"
        self.quest_points = 2

        self.agility = 51
        self.hunter = 41
        self.smithing = 54
        self.mining = 59
        self.other_requirements.append("Claim Varrock Museum kudos from Historian Minas for completing Shield of Arrav")
