import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("")])
from quests.Beneath_Cursed_Tides import Beneath_Cursed_Tides
from quests.The_Blood_Pact import The_Blood_Pact
from quests.Broken_Home import Broken_Home
from quests.Cooks_Assistant import Cooks_Assistant
from quests.The_Death_Of_Chivalry import The_Death_Of_Chivalry
from quests.Death_Plateau import Death_Plateau
from quests.Demon_Slayer import Demon_Slayer


def create_all_quests():

    beneath_cursed_tides = Beneath_Cursed_Tides()
    the_blood_pact = The_Blood_Pact()
    broken_home = Broken_Home()
    cooks_assistant = Cooks_Assistant()
    the_death_of_chivalry = The_Death_Of_Chivalry()
    death_plateau = Death_Plateau()
    demon_slayer = Demon_Slayer()

    print(beneath_cursed_tides,
          the_blood_pact,
          broken_home,
          cooks_assistant,
          the_death_of_chivalry,
          death_plateau,
          demon_slayer,
          "done")


create_all_quests()
