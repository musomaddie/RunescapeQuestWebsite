import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("questseries")])
from QuestSeriesInfo import QuestSeries


class Fremennik(QuestSeries):

    def __init__(self):
        super().__init__("Fremennik")
