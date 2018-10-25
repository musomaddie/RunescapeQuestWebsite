import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Rag_And_Bone_Man(Quest):

    def __init__(self):
        super().__init__("Rag and Bone Man")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Medium to Long"
        self.quest_points = 2
