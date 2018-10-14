import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("")])
from quests.All_Fired_Up import All_Fired_Up
from quests.Animal_Magnetism import Animal_Magnetism
from quests.Another_Slice_Of_Ham import Another_Slice_Of_Ham
from quests.As_A_First_Resort import As_A_First_Resort
from quests.Back_To_My_Roots import Back_To_My_Roots
from quests.Back_To_The_Freezer import Back_To_The_Freezer
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
from quests.Priest_In_Peril import Priest_In_Peril
from quests.The_Restless_Ghost import The_Restless_Ghost
from quests.Rune_Mysteries import Rune_Mysteries
from quests.A_Shadow_Over_Ashdale import A_Shadow_Over_Ashdale
from quests.Shield_Of_Arrav import Shield_Of_Arrav
from quests.Song_From_The_Depths import Song_From_The_Depths
from quests.A_Souls_Bane import A_Souls_Bane
from quests.Stolen_Hearts import Stolen_Hearts
from quests.Swept_Away import Swept_Away
from quests.Vampyre_Slayer import Vampyre_Slayer
from quests.Whats_Mine_Is_Yours import Whats_Mine_Is_Yours
from quests.Witchs_House import Witchs_House
from quests.Wolf_Whistle import Wolf_Whistle


def create_all_quests():

    all_fired_up = All_Fired_Up()
    animal_magnetism = Animal_Magnetism()
    another_slice_of_ham = Another_Slice_Of_Ham()
    as_a_first_resort = As_A_First_Resort()

    back_to_my_roots = Back_To_My_Roots()
    back_to_the_freezer = Back_To_The_Freezer()
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
    priest_in_peril = Priest_In_Peril()

    the_restless_ghost = The_Restless_Ghost()
    rune_mysteries = Rune_Mysteries()

    a_shadow_over_ashdale = A_Shadow_Over_Ashdale()
    shield_of_arrav = Shield_Of_Arrav()
    song_from_the_depths = Song_From_The_Depths()
    a_souls_bane = A_Souls_Bane()
    stolen_hearts = Stolen_Hearts()
    swept_away = Swept_Away()

    vampyre_slayer = Vampyre_Slayer()

    whats_mine_is_yours = Whats_Mine_Is_Yours()
    witchs_house = Witchs_House()
    wolf_whistle = Wolf_Whistle()

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
          priest_in_peril,
          the_restless_ghost,
          rune_mysteries,
          a_shadow_over_ashdale,
          shield_of_arrav,
          song_from_the_depths,
          a_souls_bane,
          stolen_hearts,
          swept_away,
          vampyre_slayer,
          whats_mine_is_yours,
          witchs_house,
          wolf_whistle,
          all_fired_up,
          another_slice_of_ham,
          animal_magnetism,
          as_a_first_resort,
          back_to_my_roots,
          back_to_the_freezer,
          "done")


create_all_quests()
