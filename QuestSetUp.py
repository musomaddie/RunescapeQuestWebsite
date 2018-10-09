import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("")])
from quests.Beneath_Cursed_Tides import Beneath_Cursed_Tides
from quests.The_Blood_Pact import The_Blood_Pact
from quests.Broken_Home import Broken_Home


def create_all_quests():

    beneath_cursed_tides = Beneath_Cursed_Tides()
    the_blood_pact = The_Blood_Pact()
    broken_home = Broken_Home()
