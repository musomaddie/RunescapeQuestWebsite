import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("")])
from quests.Beneath_Cursed_Tides import Beneath_Cursed_Tides


def create_all_quests():

    beneath_cursed_tides = Beneath_Cursed_Tides()
