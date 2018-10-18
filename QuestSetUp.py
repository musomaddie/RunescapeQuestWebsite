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
from quests.Between_A_Rock import Between_A_Rock
from quests.Big_Chompy_Bird_Hunting import Big_Chompy_Bird_Hunting
from quests.Biohazard import Biohazard
from quests.Birthright_Of_The_Dwarves import Birthright_Of_The_Dwarves
from quests.The_Blood_Pact import The_Blood_Pact
from quests.Blood_Runs_Deep import Blood_Runs_Deep
from quests.The_Branches_Of_Darkmeyer import The_Branches_Of_Darkmeyer
from quests.Bringing_Home_The_Bacon import Bringing_Home_The_Bacon
from quests.The_Brink_Of_Extinction import The_Brink_Of_Extinction
from quests.Broken_Home import Broken_Home
from quests.Buyers_And_Cellars import Buyers_And_Cellars
from quests.Cabin_Fever import Cabin_Fever
from quests.Call_Of_The_Ancestors import Call_Of_The_Ancestors
from quests.Carnillean_Rising import Carnillean_Rising
from quests.Catapult_Construction import Catapult_Construction
from quests.Children_Of_Mah import Children_Of_Mah
from quests.The_Chosen_Commander import The_Chosen_Commander
from quests.Clock_Tower import Clock_Tower
from quests.A_Clockwork_Syringe import A_Clockwork_Syringe
from quests.Cold_War import Cold_War
from quests.Contact import Contact
from quests.Cooks_Assistant import Cooks_Assistant
from quests.Creature_Of_Fenkenstrain import Creature_Of_Fenkenstrain
from quests.Crocodile_Tears import Crocodile_Tears
from quests.The_Curse_Of_Arrav import The_Curse_Of_Arrav
from quests.Darkness_Of_Hallowvale import Darkness_Of_Hallowvale
from quests.Deadliest_Catch import Deadliest_Catch
from quests.Dealing_With_Scabaras import Dealing_With_Scabaras
from quests.The_Death_Of_Chivalry import The_Death_Of_Chivalry
from quests.Death_To_The_Dorgeshuun import Death_To_The_Dorgeshuun
from quests.Death_Plateau import Death_Plateau
from quests.Defender_Of_Varrock import Defender_Of_Varrock
from quests.Demon_Slayer import Demon_Slayer
from quests.Desert_Treasure import Desert_Treasure
from quests.Devious_Minds import Devious_Minds
from quests.Diamond_In_The_Rough import Diamond_In_The_Rough
from quests.The_Dig_Site import The_Dig_Site
from quests.Dimension_Of_Disaster import Dimension_Of_Disaster
from quests.Dishonour_Among_Thieves import Dishonour_Among_Thieves
from quests.Do_No_Evil import Do_No_Evil
from quests.Dragon_Slayer import Dragon_Slayer
from quests.Dream_Mentor import Dream_Mentor
from quests.Druidic_Ritual import Druidic_Ritual
from quests.Dwarf_Cannon import Dwarf_Cannon
from quests.Eadgars_Ruse import Eadgars_Ruse
from quests.Eagles_Peak import Eagles_Peak
from quests.The_Elder_Kiln import The_Elder_Kiln
from quests.Elemental_Workshop_I import Elemental_Workshop_I
from quests.Elemental_Workshop_II import Elemental_Workshop_II
from quests.Elemental_Workshop_III import Elemental_Workshop_III
from quests.Elemental_Workshop_IV import Elemental_Workshop_IV
from quests.Enakhras_Lament import Enakhras_Lament
from quests.Enlightened_Journey import Enlightened_Journey
from quests.Ernest_The_Chicken import Ernest_The_Chicken
from quests.Evil_Daves_Big_Day_Out import Evil_Daves_Big_Day_Out
from quests.The_Eyes_Of_Glouphrie import The_Eyes_Of_Glouphrie
from quests.Fairy_Tale_I_Growing_Pains import Fairy_Tale_I_Growing_Pains
from quests.Fairy_Tale_II_Cure_A_Queen import Fairy_Tale_II_Cure_A_Queen
from quests.Fairy_Tale_III_Battle_At_Orks_Rift import Fairy_Tale_III_Battle_At_Orks_Rift
from quests.Family_Crest import Family_Crest
from quests.Fate_Of_The_Gods import Fate_Of_The_Gods
from quests.The_Feud import The_Feud
from quests.Fight_Arena import Fight_Arena
from quests.The_Firemakers_Curse import The_Firemakers_Curse
from quests.Fishing_Contest import Fishing_Contest
from quests.Forgettable_Tale import Forgettable_Tale
from quests.Forgiveness_Of_A_Chaos_Dwarf import Forgiveness_Of_A_Chaos_Dwarf
from quests.The_Fremennik_Isles import The_Fremennik_Isles
from quests.The_Fremennik_Trials import The_Fremennik_Trials
from quests.Fur_N_Seek import Fur_N_Seek
from quests.Garden_Of_Tranquillity import Garden_Of_Tranquillity
from quests.Gertrudes_Cat import Gertrudes_Cat
from quests.Ghosts_Ahoy import Ghosts_Ahoy
from quests.The_Giant_Dwarf import The_Giant_Dwarf
from quests.Glorious_Memories import Glorious_Memories
from quests.Goblin_Diplomacy import Goblin_Diplomacy
from quests.The_Golem import The_Golem
from quests.Gower_Quest import Gower_Quest
from quests.The_Grand_Tree import The_Grand_Tree
from quests.The_Great_Brain_Robbery import The_Great_Brain_Robbery
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
    between_a_rock = Between_A_Rock()
    beneath_cursed_tides = Beneath_Cursed_Tides()
    big_chompy_bird_hunting = Big_Chompy_Bird_Hunting()
    biohazard = Biohazard()
    birthright_of_the_dwarves = Birthright_Of_The_Dwarves()
    the_blood_pact = The_Blood_Pact()
    blood_runs_deep = Blood_Runs_Deep()
    the_branches_of_darkmeyer = The_Branches_Of_Darkmeyer()
    bringing_home_the_bacon = Bringing_Home_The_Bacon()
    the_brink_of_extinction = The_Brink_Of_Extinction()
    broken_home = Broken_Home()
    buyers_and_cellars = Buyers_And_Cellars()

    cabin_fever = Cabin_Fever()
    call_of_the_ancestors = Call_Of_The_Ancestors()
    carnillean_rising = Carnillean_Rising()
    catapult_construction = Catapult_Construction()
    children_of_mah = Children_Of_Mah()
    the_chosen_commander = The_Chosen_Commander()
    clock_tower = Clock_Tower()
    a_clockwork_syringe = A_Clockwork_Syringe()
    cold_war = Cold_War()
    contact = Contact()
    cooks_assistant = Cooks_Assistant()
    creature_of_fenkenstrain = Creature_Of_Fenkenstrain()
    crocodile_tears = Crocodile_Tears()
    the_curse_of_arrav = The_Curse_Of_Arrav()

    darkness_of_hallowvale = Darkness_Of_Hallowvale()
    deadliest_catch = Deadliest_Catch()
    dealing_with_scabaras = Dealing_With_Scabaras()
    the_death_of_chivalry = The_Death_Of_Chivalry()
    death_to_the_dorgeshuun = Death_To_The_Dorgeshuun()
    death_plateau = Death_Plateau()
    defender_of_varrock = Defender_Of_Varrock()
    demon_slayer = Demon_Slayer()
    desert_treasure = Desert_Treasure()
    devious_minds = Devious_Minds()
    diamond_in_the_rough = Diamond_In_The_Rough()
    the_dig_site = The_Dig_Site()
    dimension_of_disaster = Dimension_Of_Disaster()
    dishonour_among_thieves = Dishonour_Among_Thieves()
    do_no_evil = Do_No_Evil()
    dragon_slayer = Dragon_Slayer()
    dream_mentor = Dream_Mentor()
    druidic_ritual = Druidic_Ritual()
    dwarf_cannon = Dwarf_Cannon()

    eadgars_ruse = Eadgars_Ruse()
    eagles_peak = Eagles_Peak()
    the_elder_kiln = The_Elder_Kiln()
    elemental_workshop_i = Elemental_Workshop_I()
    elemental_workshop_ii = Elemental_Workshop_II()
    elemental_workshop_iii = Elemental_Workshop_III()
    elemental_workshop_iv = Elemental_Workshop_IV()
    enakhras_lament = Enakhras_Lament()
    enlightened_journey = Enlightened_Journey()
    ernest_the_chicken = Ernest_The_Chicken()
    evil_daves_big_day_out = Evil_Daves_Big_Day_Out()
    the_eyes_of_glouphrie = The_Eyes_Of_Glouphrie()

    fairy_tale_i_growing_pains = Fairy_Tale_I_Growing_Pains()
    fairy_tale_ii_cure_a_queen = Fairy_Tale_II_Cure_A_Queen()
    fairy_tale_iii_battle_at_orks_rift = Fairy_Tale_III_Battle_At_Orks_Rift()
    family_crest = Family_Crest()
    fate_of_the_gods = Fate_Of_The_Gods()
    the_feud = The_Feud()
    fight_arena = Fight_Arena()
    the_firemakers_curse = The_Firemakers_Curse()
    fishing_contest = Fishing_Contest()
    forgettable_tale = Forgettable_Tale()
    forgiveness_of_a_chaos_dwarf = Forgiveness_Of_A_Chaos_Dwarf()
    the_fremennik_isles = The_Fremennik_Isles()
    the_fremennik_trials = The_Fremennik_Trials()
    fur_n_seek = Fur_N_Seek()

    garden_of_tranquillity = Garden_Of_Tranquillity()
    gertrudes_cat = Gertrudes_Cat()
    ghosts_ahoy = Ghosts_Ahoy()
    the_giant_dwarf = The_Giant_Dwarf()
    glorious_memories = Glorious_Memories()
    goblin_diplomacy = Goblin_Diplomacy()
    the_golem = The_Golem()
    gower_quest = Gower_Quest()
    the_grand_tree = The_Grand_Tree()
    the_great_brain_robbery = The_Great_Brain_Robbery()
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

    all_quests = [beneath_cursed_tides,
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
                  between_a_rock,
                  big_chompy_bird_hunting,
                  biohazard,
                  pirates_treasure,
                  birthright_of_the_dwarves,
                  blood_runs_deep,
                  the_branches_of_darkmeyer,
                  bringing_home_the_bacon,
                  the_brink_of_extinction,
                  buyers_and_cellars,
                  cabin_fever,
                  call_of_the_ancestors,
                  carnillean_rising,
                  catapult_construction,
                  children_of_mah,
                  the_chosen_commander,
                  clock_tower,
                  a_clockwork_syringe,
                  cold_war,
                  contact,
                  creature_of_fenkenstrain,
                  crocodile_tears,
                  the_curse_of_arrav,
                  darkness_of_hallowvale,
                  deadliest_catch,
                  dealing_with_scabaras,
                  death_to_the_dorgeshuun,
                  defender_of_varrock,
                  desert_treasure,
                  devious_minds,
                  diamond_in_the_rough,
                  the_dig_site,
                  dimension_of_disaster,
                  dishonour_among_thieves,
                  do_no_evil,
                  dream_mentor,
                  dwarf_cannon,
                  eadgars_ruse,
                  eagles_peak,
                  the_elder_kiln,
                  elemental_workshop_i,
                  elemental_workshop_ii,
                  elemental_workshop_iii,
                  elemental_workshop_iv,
                  enakhras_lament,
                  enlightened_journey,
                  evil_daves_big_day_out,
                  the_eyes_of_glouphrie,
                  fairy_tale_i_growing_pains,
                  fairy_tale_ii_cure_a_queen,
                  fairy_tale_iii_battle_at_orks_rift,
                  family_crest,
                  fate_of_the_gods,
                  the_feud,
                  fight_arena,
                  the_firemakers_curse,
                  fishing_contest,
                  forgettable_tale,
                  forgiveness_of_a_chaos_dwarf,
                  the_fremennik_isles,
                  the_fremennik_trials,
                  fur_n_seek,
                  garden_of_tranquillity,
                  ghosts_ahoy,
                  the_giant_dwarf,
                  glorious_memories,
                  the_golem,
                  the_grand_tree,
                  the_great_brain_robbery,
                  "done"]
    print(all_quests)


create_all_quests()
