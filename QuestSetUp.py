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
from quests.Dragon_Slayer import Dragon_Slayer
from quests.Druidic_Ritual import Druidic_Ritual
from quests.Ernest_The_Chicken import Ernest_The_Chicken
from quests.Gertrudes_Cat import Gertrudes_Cat
from quests.Goblin_Diplomacy import Goblin_Diplomacy
from quests.Gower_Quest import Gower_Quest
from quests.Gunnars_Ground import Gunnars_Ground
from quests.Imp_Catcher import Imp_Catcher
from quests.The_Knights_Sword import The_Knights_Sword
from quests.Let_Them_Eat_Pie import Let_Them_Eat_Pie
from quests.Missing_Presumed_Death import Missing_Presumed_Death
from quests.Myths_Of_The_White_Lands import Myths_Of_The_White_Lands
from quests.One_Piercing_Note import One_Piercing_Note
from quests.Perils_Of_Ice_Mountain import Perils_Of_Ice_Mountain
from quests.Pirates_Treasure import Pirates_Treasure


def create_all_quests():

    beneath_cursed_tides = Beneath_Cursed_Tides()
    the_blood_pact = The_Blood_Pact()
    broken_home = Broken_Home()

    cooks_assistant = Cooks_Assistant()

    the_death_of_chivalry = The_Death_Of_Chivalry()
    death_plateau = Death_Plateau()
    demon_slayer = Demon_Slayer()
    dragon_slayer = Dragon_Slayer()
    druidic_ritual = Druidic_Ritual()

    ernest_the_chicken = Ernest_The_Chicken()

    gertrudes_cat = Gertrudes_Cat()
    goblin_diplomacy = Goblin_Diplomacy()
    gower_quest = Gower_Quest()
    gunnars_ground = Gunnars_Ground()

    imp_catcher = Imp_Catcher()

    the_knights_sword = The_Knights_Sword()

    let_them_eat_pie = Let_Them_Eat_Pie()

    missing_presumed_death = Missing_Presumed_Death()
    myths_of_the_white_lands = Myths_Of_The_White_Lands()

    one_piercing_note = One_Piercing_Note()

    perils_of_ice_mountain = Perils_Of_Ice_Mountain()
    pirates_treasure = Pirates_Treasure()

    print(beneath_cursed_tides,
          the_blood_pact,
          broken_home,
          cooks_assistant,
          the_death_of_chivalry,
          death_plateau,
          demon_slayer,
          dragon_slayer,
          druidic_ritual,
          ernest_the_chicken,
          gertrudes_cat,
          goblin_diplomacy,
          gower_quest,
          gunnars_ground,
          imp_catcher,
          the_knights_sword,
          let_them_eat_pie,
          missing_presumed_death,
          myths_of_the_white_lands,
          one_piercing_note,
          perils_of_ice_mountain,
          "done")


create_all_quests()
