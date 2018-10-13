import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Let_Them_Eat_Pie(Quest):

    def __init__(self):
        super().__init__("Let Them Eat Pie")
        self.age = 5
        self.free = True
